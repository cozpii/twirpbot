# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_user_tweets_location
from twirpbot import get_user_location

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		print get_verification_status(twitter, 'telegram')
	except Exception as e:
		print e
