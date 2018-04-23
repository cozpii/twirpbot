# twirpbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_date_joined

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		print get_date_joined(twitter, 'aswinmguptha')
	except Exception as e:
		print e
