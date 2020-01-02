from datetime import datetime as date_time
from dotenv import load_dotenv
from os import getenv as environment_env

load_dotenv()

class Env:
    @staticmethod
    def api_client_secret_file():
        return environment_env("API_CLIENT_SECRET_FILE")

    @staticmethod
    def api_scope():
        return [environment_env("API_SCOPE", "https://www.googleapis.com/auth/youtube.force-ssl")]

    @staticmethod
    def api_service_name():
        return environment_env("API_SERVICE_NAME", "youtube")
    
    @staticmethod
    def api_version():
        return environment_env("API_VERSION", "v3")
    
    @staticmethod
    def api_token_storage():
        return environment_env("API_TOKEN_STORAGE")

    @staticmethod
    def channel_id():
        return environment_env("CHANNEL_ID")

    @staticmethod
    def channel_url():
        return environment_env("CHANNEL_URL")

    @staticmethod
    def channel_last_video_id():
        return environment_env("CHANNEL_LAST_VIDEO_ID")

    @staticmethod
    def comment_message():
        return environment_env("COMMENT_MSG", "First!")

    @staticmethod
    def clock_time_zone():
        valid_time_zones = ["est", "gtm", "utm"]
        time_zone = environment_env("CLOCK_TIME_ZONE")

        if time_zone not in valid_time_zones:
            return valid_time_zones[0]
        
        return time_zone

    @staticmethod
    def clock_api_url():
        return "http://worldclockapi.com/api/json/{time_zone}/now".format(
            time_zone=Env.clock_time_zone()
        )

    @staticmethod
    def clock_waiting_time():
        try:
            return float(environment_env("CLOCK_WAITING_TIME"))
        except:
            return 5

    @staticmethod
    def video_release_date():
        try:
            return date_time.strptime(environment_env("VIDEO_RELEASE_DATE"), "%Y-%m-%dT%H:%M")
        except:
            print("Please, provide a valid VIDEO_RELEASE_DATE")