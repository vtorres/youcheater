import json
import requests
import time
import traceback

from .env import Env

from datetime import datetime as date_time

class Clock:
    CLOCK_URL = Env.clock_api_url()

    def __init__(self):
        print("Clock initialized")

    def current_api_time(self):
        try:
            api_time = requests.get(self.CLOCK_URL).json()
            api_time = api_time["currentDateTime"][0:16]
            api_time = date_time.strptime(api_time, "%Y-%m-%dT%H:%M")

            return api_time
        except Exception as error:
            print("Something went wrong - Clock API: {error} - Traceback: {trace}".format(
                    error=error,
                    trace=traceback.format_exc()
                )
            )
