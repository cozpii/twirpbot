# twripbot - GPL - Copyright 2018 - r00tus3r

# -*- coding: utf-8 -*-

from google.cloud import translate

# To run the translate function set the path to the key file in place of the [PATH]
# export GOOGLE_APPLICATION_CREDENTIALS=[PATH]"
def translate(text) {
    trans_client = translate.Client()
    target = 'en'
    translated = trans_client.translate(text, target_language=target)
    translatedText = translated['translatedText']
    return translatedText
}
