#!/usr/bin/python
# -*- coding: utf-8 -*-

from services.clock import Clock
from services.credentials import Credentials
from services.youtube import Youtube

if __name__ == '__main__':
    print("Youcheater!!")

    print("Clock API Time: {time}".format(time=Clock().current_api_time()))

    print("Youtube loop call with Credentials builder")
    Youtube().run()