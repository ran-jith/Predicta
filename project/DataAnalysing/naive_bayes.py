import nltk
import csv
from nltk.tokenize import word_tokenize
from pie_chart import *
from neg_tweet import *
from text_to_speech import *
from datetime import datetime
from result_collection import *
import os.path

#intialising variables and array
pos_count=0
neg_count=0
arr=[]

#read each lines of file to array

with open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\Datapreprocessing\\noise_removed_data.txt") as f:
    for line in f:
        arr.append(line)
#print(arr)

#arr=["#ElectionWatch: Union minister #NitinGadkari says the BJP and its allies would win over 300 Lok Sabha seats in the elections","But Indian election campaign looks like there's a campaign against Pakistan... Pathetic dude... #LokSabhaElections2019 #ModiBest"]
        
        
# Step 1 – Training data

"""with open('data_model.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]"""


train = negative_tweet
  
# Step 2 
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
  
# Step 4 – the classifier is trained with sample data
classifier = nltk.NaiveBayesClassifier.train(t)

#counting no of positive and negative tweets

for element in arr:
    
    test_data =element
    test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
    k=classifier.classify(test_data_features)
    if(k=="pos"):
        pos_count=pos_count+1
    else:
        neg_count=neg_count+1

        
#printing values and time
        
print("positive=",pos_count)
print("negative=",neg_count)

# To speak about result
my_speak_cloud("positive count is")
my_speak_cloud(str(pos_count))
my_speak_cloud("and the negative count is")
my_speak_cloud(str(neg_count))

date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print(date)


positive_percentage=(float(pos_count)/(pos_count+neg_count))*100

print("positive percentage=",positive_percentage)
# To speak positive percentage
my_speak_cloud("the positive percentage is obtained from this analysis is ")
my_speak_cloud(str(round(positive_percentage,2)))


positive, negative, date_, percentage = pos_count, neg_count, date, positive_percentage 
a=[positive,negative,date_,percentage]

with open('result.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(a)

csv_file.close()




pie_plot_nave_bayes(neg_count,pos_count)



