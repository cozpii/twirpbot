# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_user_location(twitter, username):
    tweet = twitter.get_user_timeline(screen_name=username, count=1)
    return tweet[0]['user']['location']
