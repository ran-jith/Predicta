#This is just a code to extract some specific tweets with known id
#by expanding the no. of id's in list we can extract the no of tweets as we needed


import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_credentials import *


# defining status id for specific tweets

input_string = input("Enter a list tweet id separated by space ")
key_input = input_string.split()
key_list=[]
for key in key_input:
    key_list.append(key)
        
   
status_id_list = key_list 



#status_id_list = ["1099082126354509826", "1099082125523992576", "1099480460772679681"]


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#creating loop to get print each data
file = open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt", "a")

for status_id in status_id_list :
    tweet = api.get_status(status_id, tweet_mode='extended')._json['full_text']
    print(tweet)
    print("\n")
    file.write(tweet)
    file.write("\n")
    
file.close()
