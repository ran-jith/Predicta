import csv
from graph_plot import *
from text_to_speech import *



#declaring two arrays

positive_result_arr=[]
positive_rvrs_result_arr=[]
date_result_arr=[]
date_rvrs_result_arr=[]

#read  values frrom csv file and store to a list

with open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataAnalysing\\result.csv','r') as csv_file:
    reader = csv.reader(csv_file)
    for i in reader:
        positive_result_arr.append(float(i[3]))
        date_result_arr.append(i[2])
        
csv_file.close()

#read last 3 values and store to new list 
positive_result_arr.reverse()
date_result_arr.reverse()

for i in range(4):
    positive_rvrs_result_arr.append(positive_result_arr[i])
    date_rvrs_result_arr.append(date_result_arr[i])



#print(rvrs_result_arr[0])
#print(date_rvrs_result_arr[0])

percentage_sum=0
for i in range(3):
    percentage_sum += (positive_rvrs_result_arr[i]-positive_rvrs_result_arr[i+1])


percentage_positive_increment = (float(percentage_sum)/4)
print("positive opinion increment in % =",percentage_positive_increment)



# To speak about result
my_speak_cloud("positive opinion increment in percentage is ")
my_speak_cloud(str(percentage_positive_increment))


plot_bar_graph(positive_rvrs_result_arr, date_rvrs_result_arr)

#To print % increment in total analysis














