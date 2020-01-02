
import requests
import time

from bs4 import BeautifulSoup as beautiful_soup

from .credentials import Credentials
from .env import Env

class Youtube:
    CHANNEL_LAST_VIDEO_ID = Env.channel_last_video_id()
    CHANNEL_ID = Env.channel_id()
    CHANNEL_URL = Env.channel_url()
    COMMENT_MESSAGE = Env.comment_message()

    NO_CACHE_HEADER = { 
        "Cache-Control": "no-cache",
        "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
        "Pragma": "no-cache"
    }

    def comment_video(self, youtube, video_id, channel_id=CHANNEL_ID, message=COMMENT_MESSAGE):
        youtube.commentThreads().insert(
            part="snippet",
            body=dict(
                snippet=dict(
                    channelId=channel_id,
                    videoId=video_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=message
                        )
                    )
                )
            )
        ).execute()
    
    def like_video(self, youtube, video_id):
        youtube.videos().rate(rating='like', id=video_id).execute()
    
    def get_latest_video_id(self):
        href_finder = lambda link: link.attrs['href']
        watch_finder = lambda ahref: ahref.startswith('/watch?v=')

        try:
            request = requests.get(self.CHANNEL_URL, headers=self.NO_CACHE_HEADER)
            soup = beautiful_soup(request.text, "html.parser")
            hrefs = next(filter(watch_finder, map(href_finder, soup.find_all('a'))))
            video_id = hrefs[-11:]
            
            return video_id
        except (AttributeError, KeyError, TypeError):
            return 0

    def run(self):
        try:
            credentials = Credentials.build()
            latest_video_id = self.get_latest_video_id()
            is_new_release = latest_video_id != self.CHANNEL_LAST_VIDEO_ID and latest_video_id != 0

            if is_new_release:
                self.comment_video(credentials, latest_video_id)
                self.like_video(credentials, latest_video_id)
                print("Leeroy Jenkins! Comment/Like created")
            else:
                print(
                    "No news video releases yet - still video_id = {video_id}".format(
                        video_id=latest_video_id
                    )
                )
                
                self.run()
        except KeyboardInterrupt:
            print("Exited by the user.")
        except Exception as e:
            print("Request error gone wrong. Auto continue ;) {e}".format(e=e))
            self.run()
        