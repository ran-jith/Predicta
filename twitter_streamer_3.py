#This is just a code to extract some specific tweets with known id
#by expanding the no. of id's in list we can extract the no of tweets as we needed


import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_credentials import *


# defining status id for specific tweets


status_id_list = ["10990xxxxxxxxx", "1099082125xxxxxxxxx", "10994804607xxxxxxx"]


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#creating loop to get print each data
file = open("tweets.txt", "a")

for status_id in status_id_list :
    tweet = api.get_status(status_id, tweet_mode='extended')._json['full_text']
    print(tweet)
    print("\n")
    file.write(tweet)
    file.write("\n")
    
file.close()
