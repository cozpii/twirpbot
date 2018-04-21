# twripbot - GPL - Copyright 2018 - aswinmguptha
from twython import Twython
import utils

def get_link_in_bio(twitter, username):
	user_info = twitter.show_user(screen_name=username)
        if 'url' in user_info['entities']:
                print user_info['entities']['url']['urls'][0]['expanded_url']
if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_link_in_bio(twitter, 'telegram.org')
	except Exception as e:
		print e
