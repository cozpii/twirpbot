# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_followings_list(twitter, username, count_per_req):
	followings_list = []
	friends = twitter.get_friends_list(screen_name=username, count=count_per_req)
	for i in xrange(count_per_req):
		followings_list.append(friends['users'][i]['screen_name'])
	return followings_list
