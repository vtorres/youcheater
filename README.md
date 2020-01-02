<div align="center">

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/vtorres/youcheater)

</div>

<h1 align="center">

![](https://i.imgur.com/OWPF3I3.png)

</h1>

<div align="center">

[![Python 3.9](https://img.shields.io/badge/python-3.9-00acd2.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2bd8af.svg)](https://github.com/vtorres/youcheater/blob/master/LICENSE)

</div>

<h3 align="center">
  💬 Auto Comment/Like for Youtube Contests | ZHC | MrBeast 💬
</h3>

The YouTube channels that gained the most subscribers in the latest year show the platform's current trends
and the areas that are growing rapidly. YouTube channels like MrBeast and ZHC are known by giving prizes
away to the subscribers and for whatever reasons, channels have sort of gamified the objective
of having the first comment/like on a video as soon as it releases!
Yeah, you know... here it comes the automation step! Using a Python command-line application that crawls the data out of YouTube
and search for the latest video of the specified YouTube channel with the goal to auto comment/like using
the YouTube API Provider.

### Install dependencies

- Only needs this step if you started without the use of Gitpod:
```
pip install -r requirements.txt
```

### Configure

- Replace the client_id.json file inside the credentials directory by your google credentials generated file

- Change the following variables in the .env file:
```
CHANNEL_ID # Youtube Channel ID
CHANNEL_URL # Youtube Channel URL
CHANNEL_LAST_VIDEO_ID # Youtube Channel Current Last Video ID
CLOCK_TIME_ZONE # est gmt or utc
CLOCK_WAITING_TIME # Verification period time in seconds
COMMENT_MSG # Your comment
VIDEO_RELEASE_DATE # Start time to try to scrape the data out of youtube
```


### Run
- Use with your responsibility:
```
python ./src/youcheater.py
```

### Contributors
- There are many ways to improve this project, feel free to contribute with your pull request

| Author | Description |
| :---: | :--- |
| <img src="https://avatars1.githubusercontent.com/u/3085197?s=460&v=4" width="75"> | **One day project by [@vtorres](https://github.com/vtorres)**