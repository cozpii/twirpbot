# twirpbot - GPL - Copyright 2018 - aswinmguptha

from time import strptime, mktime
from collections import Counter

def get_most_common_retweet_frequency(twitter, username, max_count):
    earlier_tweet_id = 0
    tweet_count = 0
    tweet_id_list = []
    timestamp = 0
    tweet_timestamp = []
    tweet_frequency = 0
    frequency = []
    frequency_count = []

    while max_count > tweet_count:
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, tweet_mode='extended', exclude_replies='false', include_rts='true')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='false', include_rts='true')

        for tweet in tweets:
            tweet_count += 1
            tweet_id_list.append(tweet['id'])

            if tweet['full_text'].strip().split()[0] == 'RT':
                timestamp = int(mktime(strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')))
                tweet_timestamp.append(timestamp)

                if len(tweet_timestamp) > 1:
                    tweet_frequency = (tweet_timestamp[len(tweet_timestamp) - 2] - tweet_timestamp[len(tweet_timestamp) - 1]) / (60*60)
                    frequency.append(tweet_frequency)

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break

    frequency_count = Counter(frequency)
    return frequency_count.most_common(5)
