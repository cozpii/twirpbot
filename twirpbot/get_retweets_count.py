# twirpbot - GPL - Copyright 2018 - aswinmguptha, r00tus3r

def get_retweets_count(twitter, username):
    max_count = 1000000
    earlier_tweet_id = 0
    tweet_count = 0
    tweet_id_list = []
    retweets_count = 0

    while max_count > tweet_count:
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, tweet_mode='extended', exclude_replies='true', include_rts='true')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='true', include_rts='true')

        for tweet in tweets:
            tweet_count += 1
            tweet_id_list.append(tweet['id'])
            if tweet['full_text'].strip().split()[0] == 'RT':
                retweets_count += 1

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break

    return retweets_count
