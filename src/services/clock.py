import json
import requests
import time
import traceback

from .env import Env

from datetime import datetime as date_time

class Clock:
    CLOCK_URL = Env.clock_api_url()
    TICK_TIME = Env.clock_waiting_time()
    RELEASE_DATE = Env.video_release_date()

    def __init__(self, service):
        self.service = service

    def wait_and_log(self):
        time.sleep(self.TICK_TIME)

        print(
            "Checking... | Release Date: {release_date} | Hour now: {hour_now}".format(
                release_date=self.RELEASE_DATE,
                hour_now=self.current_api_time()
            )
        )

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

    def cron(self):
        try:
            self.wait_and_log()

            is_ready_for_release = self.current_api_time() >= self.RELEASE_DATE

            self.service().run() if is_ready_for_release else self.cron()
        except Exception as error:
            print(
                "Something went wrong - Clock Cron: {error} - Traceback: {trace}".format(
                    error=error,
                    trace=traceback.format_exc()
                )
            )

