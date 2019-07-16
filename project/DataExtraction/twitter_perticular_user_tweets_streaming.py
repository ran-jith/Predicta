from authentication import *
from speech_to_text import *




#USER_ID="BarackObama"                                      #This is the username of user starting with '@'

print("enter user id=")
USER_ID=input()

try:
    
    data = api.get_user(USER_ID)

    print ("Followers:" + str(data.followers_count))
    print ("Tweets:" + str(data.statuses_count))
    print ("Favourites:" + str(data.favourites_count))
    print ("Friends:" + str(data.friends_count))



    file = open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt", "a")


    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=USER_ID, tweet_mode="extended").items():
            print(status.full_text)
            file.write(status.full_text)
            file.write("\n")

    except BaseException as e:
        print("Error on_data %s" % str(e))
        

    file.close()

except:

    print("User ID is wrong. Try Again.")
