# twripbot - GPL - Copyright 2018 - aswinmguptha
from twython import Twython
import utils

def get_tweets_count(twitter, username):
	user_info = twitter.show_user(screen_name=username)
        print user_info['statuses_count']

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_tweets_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
