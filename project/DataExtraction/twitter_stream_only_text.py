from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

 
import twitter_credentials
import json
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.fetched_tweets_filename = fetched_tweets_filename
        

    def on_data(self, data):

        self.num_tweets += 1
        if self.num_tweets < 30:
        
            try:
            
                data = json.loads(data)
                text=data['extended_tweet']['full_text']
                print(text)
                #print(data['extended_tweet']['full_text'])
                with open(self.fetched_tweets_filename, 'a') as tf:
                    #json_load = json.loads(data)
                    #print(json_load.text)
                    tf.write(text)
                
                return True
            except BaseException as e:
                print("Error on_data %s" % str(e))
            return True
        else:
            return False
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.

    input_string = input("Enter a list of keywords separated by space ")
    key_input = input_string.split()
    key_list=[]
    for key in key_input:
        key_list.append(key)
        
    
    hash_tag_list = key_list 
    
    #hash_tag_list = ["game of thrones","seasons","climax","lastt season"]
    fetched_tweets_filename = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    
    
