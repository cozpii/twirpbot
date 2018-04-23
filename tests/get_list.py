# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_followers_list
from twirpbot import get_followings_list
from twirpbot import get_timeline_tweets

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		print get_followers_list(twitter, 'aswinmguptha', 2)
	except Exception as e:
		print e
	try:
		print get_followings_list(twitter, 'aswinmguptha', 2)
	except Exception as e:
		print e
	try:
		print get_timeline_tweets(twitter, 'aswinmguptha', 200)
	except Exception as e:
		print e
