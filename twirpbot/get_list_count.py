# twripbot - GPL - Copyright 2018 - r00tus3r

def get_list_count(twitter, username):
	user_info = twitter.show_user(screen_name=username)
	return user_info['listed_count']
