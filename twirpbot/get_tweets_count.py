# twripbot - GPL - Copyright 2018 - aswinmguptha

def get_tweets_count(twitter, username):
	user_info = twitter.show_user(screen_name=username)
    return user_info['statuses_count']
