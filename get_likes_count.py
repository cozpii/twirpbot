# twripbot - GPL - Copyright 2018 - abx1
from twython import Twython
import utils

def get_likes_count(twitter, username):
	likes_count = twitter.show_user(screen_name=username)
        print likes_count['favourites_count']

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_likes_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
