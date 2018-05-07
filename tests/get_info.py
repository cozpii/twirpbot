# twirpbot - GPL - Copyright 2018 - r00tus3r
# -*- coding: utf-8 -*-

from twirpbot import *

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e

	username = 'lekshmisingh'

	all_followings = get_followings_list(twitter, username, 1000)

	f = open('cozpii_data', 'w')

	f.write('screen_name``` no. of tweets``` no. of retweets``` no. of followers``` no. of following``` no. of likes``` date of joining``` link in bio``` link in description``` no. of replies``` no. of media tweets``` most occuring word in tweet``` most occuring word in retweet``` user location``` no. of list``` verification status\n')

	cnt = 0

	#for name in all_followings:
	for i in xrange(len(all_followings)):
		name = all_followings[i+5]
		print str(cnt) +' Collecting data of ' + name
		cnt += 1
		dataset = ''
		dataset += name + '``` ' + str(get_tweets_count(twitter, name)) + '``` '
		dataset += str(get_retweets_count(twitter, name)) + '``` ' +  str(get_followers_count(twitter, name)) + '``` '
		dataset +=  str(get_followings_count(twitter, name)) + '``` ' + str(get_likes_count(twitter, name)) + '``` '
		dataset +=	str(get_date_joined(twitter, name)) + '``` '
		tmp = get_link_in_bio(twitter, name)
		if ( tmp != None):
			dataset += str(tmp.encode('utf-8')) + '``` '
		else:
			dataset += str(tmp) + '``` '
		tmp = get_link_in_description(twitter, name)
		if (tmp != None):
			dataset += str(tmp.encode('utf-8'))
		else:
			dataset += str(tmp)
		dataset += '``` ' + str(get_replies_count(twitter, name)) + '``` '
		dataset += str(get_media_tweets_count(twitter, name, 100000)) + '``` '
		tmp = get_most_common_unigrams_in_tweets(twitter, name, 100000)
		if (tmp != None):
			tmp = translate(tmp.encode('utf-8'))
			dataset += str(tmp) + '``` '
		else:
			dataset += str(tmp) + '``` '
		tmp = get_most_common_unigrams_in_retweets(twitter, name, 100000)
		if (tmp != None):
			tmp = translate(tmp.encode('utf-8'))
			dataset += str(tmp) + '``` '
		else:
			dataset += str(tmp) + '``` '
		if (get_user_location(twitter, name) == ''):
			dataset += 'False'
		else:
			dataset += 'True'
		dataset += '``` ' + str(get_list_count(twitter, name)) + '``` '
		dataset += str(get_verification_status(twitter, name))
		dataset += '\n'
		print dataset
		f.write(dataset)
