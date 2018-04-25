# twirpbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_followings_list
from twirpbot import get_tweets_count
from twirpbot import get_retweets_count
from twirpbot import get_replies_count

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	username = 'lekshmisingh'
	all_followings = get_followings_list(twitter, username, 100)
	for i in all_followings:
		print i + ' ' + str(get_tweets_count(twitter, i)) + ' ' + str(get_retweets_count(twitter, i)) + ' ' + str(get_replies_count(twitter, i))
