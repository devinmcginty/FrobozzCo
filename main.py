#!/usr/bin/env python3.4
# -*- coding: utf-8 -*- #
import tweepy
from auth import *

cKey = CREDENTIALS[C_KEY]
cSecret = CREDENTIALS[C_SECRET]
aToken = CREDENTIALS[A_TOKEN]
aSecret = CREDENTIALS[A_SECRET]

class Listener(tweepy.streaming.StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

class Frobot(object):
    def __init__(self):
        self.api = None
        self.authenticate()
    def authenticate(self):
        auth = tweepy.OAuthHandler(cKey, cSecret)
        auth.set_access_token(aToken, aSecret)
        self.api = tweepy.API(auth)

if __name__ == '__main__':
    Frobot()
