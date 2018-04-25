# twirpbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_count_of_hashtags_per_user
from twirpbot import get_followers_count
from twirpbot import get_followings_count
from twirpbot import get_likes_count
from twirpbot import get_tweets_count
from twirpbot import get_list_count
from twirpbot import get_media_tweets_count
from twirpbot import get_replies_count
from twirpbot import get_retweets_count
from twirpbot import get_most_common_tweet_frequency

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		print get_count_of_hashtags_per_user(twitter, 'aswinmguptha', 'nullcon')
	except Exception as e:
		print e
	try:
		print get_followers_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_followings_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_likes_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_tweets_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_list_count(twitter, 'a0xnirudh')
	except Exception as e:
		print e
	try:
		print get_media_tweets_count(twitter, 'aswinmguptha', 400)
	except Exception as e:
		print e
	try:
		print get_replies_count(twitter, 'aswinmguptha', 400)
	except Exception as e:
		print e
	try:
		print get_retweets_count(twitter, 'aswinmguptha', 400)
	except Exception as e:
		print e
	try:
		print get_most_common_tweet_frequency(twitter, 'aswinmguptha', 400)
	except Exception as e:
		print e
