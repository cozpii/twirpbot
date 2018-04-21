from twython import Twython
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
from nltk import ngrams
from pymongo import MongoClient
import utils

def save_tweet_mongo(tweet):
	client = MongoClient()
	db = client.pk_tweets
	post = tweet
    post['_id'] = tweet['id']
	try:
		db.tweets_collected.insert(post)
	except Exception as exc:
		print exc

def get_timeline_tweets(username, cnt):
	while max_count > tweet_count:
		tweet_id_list = []

		if earlier_tweet_id <= 0:
			tweets = twitter.get_user_timeline(screen_name=username, count=200, tweet_mode='extended', exclude_replies='true')
		else:
			tweets = twitter.get_user_timeline(screen_name=username, count=200, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

		for tweet in tweets:
			tweet_count += 1

		if(len(tweets)):
			earlier_tweet_id = sorted(tweet_id_list)[0]
		else: tweet_count=max_count

#to do
def get_followers():
	twitter.get_followers_list(screen_name=username)

if __name__ == '__main__':

	#initialising twython
	try:
		twitter = utils.connect()
	except Exception as e:
		print e

	max_count = 1900 #the no of tweets to be retrieved
	earlier_tweet_id = 0
	tweet_count = 0
	bigrams = []
