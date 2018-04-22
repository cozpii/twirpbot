# twripbot - GPL - Copyright 2018 - aswinmguptha

def get_link_in_description(twitter, username):
	user_info = twitter.show_user(screen_name=username)
	description = user_info['description']
	if len(user_info['entities']['description']['urls']) > 0:
		for i in range(len(user_info['entities']['description']['urls'])):
			print user_info['entities']['description']['urls'][i]['expanded_url']
