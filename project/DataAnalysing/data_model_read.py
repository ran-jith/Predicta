import csv


'''data=[]
with open('result.csv') as fp:
    for line in fp:
        #data.append(line)
        #print(data)
        print(line[1,2])'''

import csv
with open('data_model.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]
print (data)
