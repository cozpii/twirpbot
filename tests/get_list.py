# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_followers_list
from twirpbot import get_followings_list

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
		get_followings_list(twitter, 'aswinmguptha', 2)
	except Exception as e:
		print e
