

import tweepy
from textblob import TextBlob



consumer_key = 'Kv72JhMpzpmjTSxmodudSss5X'
consumer_secret = '5a0Bf57RTzYiVDI97iT8OGTve4ZD2bOZOakvaV9xcYYDlZPN3o'

access_token = '519080160-GnrzCFVJZhDSexK8TuT5gvNjBOvxQqcYwKHDp8zV'
access_token_secret = 'f00oJG9QhJetKc7EGvHVleQNubdxos4GsFKolpBgGBswY'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


