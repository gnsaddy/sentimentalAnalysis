import sys
import matplotlib.pyplot as plt
from textblob import TextBlob
from pprint import pprint
import json
import re
from tweepy import OAuthHandler
import tweepy
#from __future__ import absolute_import, print_function

#Authentication
consumer_key = 'Kv72JhMpzpmjTSxmodudSss5X'
consumer_secret = '5a0Bf57RTzYiVDI97iT8OGTve4ZD2bOZOakvaV9xcYYDlZPN3o'
access_token = '519080160-GnrzCFVJZhDSexK8TuT5gvNjBOvxQqcYwKHDp8zV'
access_token_secret = 'f00oJG9QhJetKc7EGvHVleQNubdxos4GsFKolpBgGBswY'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


kt = {}

tweets = tweepy.Cursor(api.search, q="Karnataka elections", count=200,
                       lang="en").items(200)


def clean_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


counter = 0


positive = 0
negative = 0
neutral = 0

'''try:'''
for tweet in tweets:
		counter += 1
		blob = TextBlob(tweet.text)
		#pprint(tweet.text)
		polarity = blob.sentiment.polarity
		#pprint('\n'+"Sentiment is:"+str(polarity))
		if polarity > 0.0:
			positive += 1
		elif polarity < 0.0:
			negative += 1
		else:
			neutral += 1
		file = open('TweetData\\tweet'+'.csv', 'a')
		#tweet.text= tweet.text.encode("utf-8",'ignore').decode('utf-8','ignore')
		tweet.text = clean_tweet(tweet.text)
		tweet.text = bytes(tweet.text, 'utf-32').decode('utf-32', 'replace')
		file.write(tweet.text)
		file.write('\n')
		file.close()
		#print('\n\n')
'''except:
	print("Still getting a naughty error")'''
#text=text.replace('\xc2\xa0', ' ')
#new_str = unicodedata.normalize("NFKD", unicode_str)

print(str(counter)+" Tweets fetched successfully")
print('\n\n')


def perc(x, y): return float(x)*100.0/float(y)


positive = perc(positive, counter)
negative = perc(negative, counter)
neutral = perc(neutral, counter)


print(positive, negative, neutral)


x = [positive, negative, neutral]

plt.pie(x, labels=["positive", "negative", "neutral"])
plt.show()
plt.bar([1, 2, 3], height=x, tick_label=["positive", "negative", "neutral"])
plt.show()
