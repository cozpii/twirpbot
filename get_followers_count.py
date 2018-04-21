# twripbot - GPL - Copyright 2018 - abx1
from twython import Twython
import utils

def get_followers_count(twitter, username):
	followers_count = twitter.show_user(screen_name=username)
        print followers_count['followers_count']

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_followers_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
