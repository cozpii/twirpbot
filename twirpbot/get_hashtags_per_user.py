# twirpbot - GPL - Copyright 2018 - r00tus3r

def get_hashtags_per_user(twitter, username):
    max_count = 100000 # the no of tweets to be retrieved
    earlier_tweet_id = 0
    tweet_count = 0
    tweet_id_list = []
    hashtag_cnt = 0

    while max_count > tweet_count:
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, tweet_mode='extended', exclude_replies='false')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=200, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='false')

        for tweet in tweets:
            print 'Tweet: ' + tweet['full_text']
            print 'No. of hashtags: ' + str(len(tweet['entities']['hashtags']))

            if (len(tweet['entities']['hashtags']) > 0):
                print 'Hashtags found:'
                for i in xrange(len(tweet['entities']['hashtags'])):
                    print tweet['entities']['hashtags'][i]['text']
            print '\n'
            tweet_count += 1
            tweet_id_list.append(tweet['id'])

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break
