# twirpbot - GPL - Copyright 2018 - abx1, r00tus3r

def get_followers_list(twitter, username, count_per_req):
	followers_list = []
	followers = twitter.get_followers_list(screen_name=username, count=count_per_req)
	for i in xrange(count_per_req):
		followers_list.append(followers['users'][i]['screen_name'])
	return followers_list
