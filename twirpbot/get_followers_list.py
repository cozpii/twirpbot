# twirpbot - GPL - Copyright 2018 - abx1, r00tus3r

def get_followers_list(twitter, username, count_per_req):
	cur = 0
	count = 0
	followers_list = []

	while count_per_req > count:
		if cur == 0:
			followers = twitter.get_followers_list(screen_name=username, count=200)
		else:
			followers = twitter.get_followers_list(screen_name=username, count=200, cursor = cur)

		for i in xrange(len(followers['users'])):
			followers_list.append(followers['users'][i]['screen_name'])

		count += len(followers['users'])

		if (len(followers['users']) and followers['next_cursor'] != 0):
			cur = followers['next_cursor']
		else:
			break

	return followers_list
