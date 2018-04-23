# twirpbot - GPL - Copyright 2018 - aswinmguptha

def get_link_in_bio(twitter, username):
	user_info = twitter.show_user(screen_name=username)
	if 'url' in user_info['entities']:
		print user_info['entities']['url']['urls'][0]['expanded_url']
