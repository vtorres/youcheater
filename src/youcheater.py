#!/usr/bin/python
# -*- coding: utf-8 -*-

from services.credentials import Credentials
from services.clock import Clock
from services.youtube import Youtube

if __name__ == '__main__':
    Credentials.build()
    
    Clock(service=Youtube).cron()