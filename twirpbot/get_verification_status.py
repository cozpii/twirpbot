# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_verification_status(twitter, username):
	user_info = twitter.show_user(screen_name=username)
	return user_info['verified']
