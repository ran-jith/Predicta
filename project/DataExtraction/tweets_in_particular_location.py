from authentication import *




print("enter a key value")
input_key = str(input())


file = open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt", "a")
class CustomStreamListener(tweepy.StreamListener):
    tweet_counter = 0
    stop_at=100
    
    def on_status(self, status):
        CustomStreamListener.tweet_counter+=1
        word_list=input_key
        #if word_list in status.text.lower():
            #print (status.text)

        if CustomStreamListener.tweet_counter < CustomStreamListener.stop_at:
            if word_list in status.text.lower():
                print (status.text)
                file.write(status.text)
                file.write("\n")

            return True
        else:
            print('Max num reached = ' + str(CustomStreamListener.tweet_counter))
            return False
        

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(), tweet_mode='extended')


"""input_string = input("Enter a list location coordinates separated by space ")
key_input = input_string.split()
key_list=[]
for key in key_input:
    key_list.append(float(key))
        

sapi.filter(locations=key_list, languages=["en"])"""
sapi.filter(locations=[36.5228181087,-6.7034077969,105.3458974546,50.8153129593], languages=["en"])

file.close()
