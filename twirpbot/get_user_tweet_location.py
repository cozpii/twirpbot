# twripbot - GPL - Copyright 2018 - r00tus3r

def get_user_tweets_location(twitter, username):
    max_count = 1000000 # the no of tweets to be retrieved
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
            if tweet['place'] != None:
                print 'Location: ' + str(tweet['place']['full_name'])
            else:
                print 'No tweet location found'
            tweet_count += 1
            tweet_id_list.append(tweet['id'])

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break
