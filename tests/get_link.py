# twirpbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_link_in_bio
from twirpbot import get_link_in_description
from twirpbot import get_image_url_in_tweets

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		get_link_in_bio(twitter, 'telegram')
	except Exception as e:
		print e
	try:
		get_link_in_description(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_image_url_in_tweets(twitter, 'aswinmguptha', '200')
	except Exception as e:
		print e
