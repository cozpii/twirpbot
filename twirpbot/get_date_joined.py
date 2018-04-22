# twripbot - GPL - Copyright 2018 - abx1

def get_date_joined(twitter, username):
	user_info = twitter.show_user(screen_name=username)
        return str(user_info['created_at'])
