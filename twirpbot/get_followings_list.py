# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_followings_list(twitter, username, count_per_req):
	followings_list = []
	cur = 0
	count = 0

	while count_per_req > count:
		if cur == 0:
			friends = twitter.get_friends_list(screen_name=username, count=200)
		else:
			friends = twitter.get_friends_list(screen_name=username, count = 200, cursor = cur)

		if (len(friends['users']) and friends['next_cursor'] != 0):
			cur = friends['next_cursor']
		else:
			break

		for i in xrange(len(friends['users'])):
			followings_list.append(friends['users'][i]['screen_name'])

		count += len(friends['users'])

	return followings_list
