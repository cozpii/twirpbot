# twirpbot - GPL - Copyright 2018 - abx1
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

def translate(to_translate, to_language="auto", from_language="auto"):

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
