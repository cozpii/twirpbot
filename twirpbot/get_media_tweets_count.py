# twirpbot - GPL - Copyright 2018 - aswinmguptha

def get_media_tweets_count(twitter, username, max_count):
    earlier_tweet_id = 0
    tweet_count = 0
    tweet_id_list = []
    media_count = 0

    while max_count > tweet_count:
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, tweet_mode='extended', exclude_replies='false', include_rts='false')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='false', include_rts='false')

        for tweet in tweets:
            tweet_count += 1
            tweet_id_list.append(tweet['id'])
            if 'media' in tweet['entities']:
                media_count += 1

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break

    return media_count
