# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_timeline_tweets(twitter, username, max_count):
    earlier_tweet_id = 0
    tweet_count = 0
    tweet_id_list = []
    all_tweets = []

    while max_count > tweet_count:
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=100, tweet_mode='extended', exclude_replies='false')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=100, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='false')

        for tweet in tweets:
            all_tweets.append(tweet['full_text'])
            tweet_count += 1
            tweet_id_list.append(tweet['id'])

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break

    return all_tweets
