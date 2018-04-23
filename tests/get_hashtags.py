# twirpbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_hashtags_per_user

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		get_hashtags_per_user(twitter, 'aswinmguptha')
	except Exception as e:
		print e
