#!/usr/bin/python
# -*- coding: utf-8 -*-

from services.env import Env

if __name__ == '__main__':
    print("Youcheater!!")
    print("Message: #{comment}".format(comment=Env.comment_message()))