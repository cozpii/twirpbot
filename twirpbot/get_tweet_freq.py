# twirpbot - GPL - Copyright 2018 - abx1

from twirpbot import connect 
from datetime import datetime

def get_timeline_tweets(twitter, username):
    max_count = 10 # the no of tweets to be retrieved
    earlier_tweet_id = 0
    tweet_count = -1
    tweet_id_list = []
    tweet_time_list = []
    frequency = []

    while max_count > tweet_count:
        loop = 1
        cnt = 0
        if earlier_tweet_id <= 0:
            tweets = twitter.get_user_timeline(screen_name=username, count=5, tweet_mode='extended', exclude_replies='false')
        else:
            tweets = twitter.get_user_timeline(screen_name=username, count=5, max_id=earlier_tweet_id-1, tweet_mode='extended', exclude_replies='false')

        for tweet in tweets:
            tweet_count += 1
            tweet_time_list[tweet_count] = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
            
            #check if the previous three tweets were on the same day
            if tweet_count >= 3:
                while(loop < 3):
                    if tweet_time_list[tweet_count][:10] == tweet_time_list[tweet_count-loop][:10]:    
                        cnt = cnt +1;
                    loop=loop+1
                frequency.append(cnt)
            tweet_id_list.append(tweet['id'])

        if(len(tweets)):
            earlier_tweet_id = sorted(tweet_id_list)[0]
        else:
            break

if __name__ == '__main__':
    get_timeline_tweets(connect(), "aswinmguptha")
