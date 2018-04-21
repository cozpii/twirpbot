# twripbot - GPL - Copyright 2018 - aswinmguptha
from twython import Twython
import utils

def get_link_in_bio(twitter, username):
	user_info = twitter.show_user(screen_name=username)
        description = user_info['description']
        if len(user_info['entities']['description']['urls']) > 0:
                for i in range(len(user_info['entities']['description']['urls'])):
                        print user_info['entities']['description']['urls'][i]['expanded_url']
if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_link_in_bio(twitter, 'rinkuaravind')
	except Exception as e:
		print e
