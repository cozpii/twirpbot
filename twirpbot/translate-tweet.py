# twripbot - GPL - Copyright 2018 - abx1
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

if __name__ == '__main__':
    try:
        print translate("अगर हम मोक्ष चाहते हैं तो हमें उस संत की शरण ग्रहण करनी चाहिए जिसकी शरण में जाने से पूर्ण परमात्मा की प्राप्ति हो वह भी हमारे शास्त्रों अनुसार कौन है वह संत जानने के लिए अवश्य देखिए श्रद्धा टीवी दोपहर 2:00 बजे।", "en")
    except Exception as e:
        print e

