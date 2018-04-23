# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect

def get_followings_list(twitter, username, count_per_req):
	followings_list = []
	friends = twitter.get_friends_list(screen_name=username, count=count_per_req)
	for i in xrange(count_per_req):
		followings_list.append(friends['users'][i]['screen_name'])
	return followings_list

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e

	try:
		print get_followings_list(twitter, 'aswinmguptha', 2)
	except Exception as e:
		print e
