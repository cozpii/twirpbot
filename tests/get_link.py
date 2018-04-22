# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_link_in_bio
from twirpbot import get_link_in_description

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
		get_link_in_description(twitter, 'rinkuaravind')
	except Exception as e:
		print e
