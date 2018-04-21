# twripbot - GPL - Copyright 2018 - abx1
from twython import Twython
import utils

def get_date_joined(twitter, username):
	date_joined = twitter.show_user(screen_name=username)
        print date_joined['created_at']

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_date_joined(twitter, 'aswinmguptha')
	except Exception as e:
		print e
