# twripbot - GPL - Copyright 2018 - r00tus3r
# -*- coding: utf-8 -*-

from google.cloud import translate
from twython import Twython

# To run the translate function set the path to the key file in place of the [PATH]
# export GOOGLE_APPLICATION_CREDENTIALS=[PATH]"
def translate(text):
    translate_client = translate.Client()
    target = 'en'
    translated = translate_client.translate(text, target_language=target)
    translatedText = translated['translatedText']
    return translatedText

# Add the tokens in the tokens file
def connect():
    f = open('tokens', 'r')
    consumer_key = f.readline().strip().split('=')[1].replace(' ', '')
    consumer_key_secret = f.readline().strip().split('=')[1].replace(' ', '')
    access_token = f.readline().strip().split('=')[1].replace(' ', '')
    access_token_secret = f.readline().strip().split('=')[1].replace(' ', '')
    return Twython(consumer_key, consumer_key_secret, access_token, acc_token_secret)
