# twirpbot - GPL - Copyright 2018 - r00tus3r

from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams

def get_most_common_unigrams_in_tweets(name, maxTweets):
    stopwords_english = stopwords.words('english')
    id_of_earliest_tweet = None
    count = 0
    list_of_tweets = []
    all_unigrams = []
    all_unigrams_without_noise = []
    all_stemmed_unigrams = []
    stemmer = PorterStemmer()
    new_statuses = []

    while count < maxTweets:
        if id_of_earliest_tweet <= 0:
            statuses = twitter.get_user_timeline(screen_name=name, count="100", tweet_mode='extended', include_rts='false', exclude_replies='false')

        else:
            statuses = twitter.get_user_timeline(screen_name=name, count="100", tweet_mode='extended', max_id=id_of_earliest_tweet - 1, include_rts='false', exclude_replies='false')

        new_statuses += statuses

        for tweet in statuses:
            count += 1
            list_of_tweets.append(tweet['id'])

        if(len(statuses)):
            id_of_earliest_tweet = sorted(list_of_tweets)[0]
        else:
            break

    for tweet in new_statuses:
        unigrams = word_tokenize(tweet['full_text'].lower())
        all_unigrams += unigrams

    for word in all_unigrams:
        stemmed_unigram = stemmer.stem(word)
        all_stemmed_unigrams.append(stemmed_unigram)

    for word in all_stemmed_unigrams:
        if word in stopwords_english or len(word) < 4 or 'http' in word or 'www' in word or '//' in word:
            continue
        else:
            all_unigrams_without_noise.append(word)

    all_unigrams_list = list(ngrams(all_unigrams_without_noise,1))
    frequencies = Counter(all_unigrams_list)
    for token,count in frequencies.most_common(10):
        print token,count
