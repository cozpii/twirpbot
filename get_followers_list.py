# twripbot - GPL - Copyright 2018 - abx1
from twython import Twython
import utils

def get_followers(twitter, username, count_per_req):
	followers = twitter.get_followers_list(screen_name=username, count=count_per_req)

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_followers(twitter, 'aswinmguptha', 2)
	except Exception as e:
		print e