# twirpbot - GPL - Copyright 2018 - r00tus3r
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
from twython import Twython

def translate(to_translate, to_language="en", from_language="auto"):

    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    to_translate = requests.utils.requote_uri(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    try:
    	result = requests.get(link)
    except Exception as e:
    	print("Couldn't connect to translation server\n")
    data = result.content
    soup = bs(data, "lxml")
    result = soup.find_all("div", "t0")
    result = str(result[0])[26:-6]
    return result

# Add the tokens in the tokens file
def connect():
    f = open('/home/r00tus3r/git/twirpbot/tokens', 'r')
    consumer_key = f.readline().strip().split('=')[1].replace(' ', '')
    consumer_key_secret = f.readline().strip().split('=')[1].replace(' ', '')
    access_token = f.readline().strip().split('=')[1].replace(' ', '')
    access_token_secret = f.readline().strip().split('=')[1].replace(' ', '')
    return Twython(consumer_key, consumer_key_secret, access_token, access_token_secret)
