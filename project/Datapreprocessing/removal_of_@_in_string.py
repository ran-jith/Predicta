import re, string, unicodedata





#f = open("C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\DataExtraction\project\tweets.txt", "r")
f = open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt", "r")
s=f.read()
f.close()

#print(re.sub(r'\[image.+image\]','',s))
#print(re.sub(r'\@\', '', s))
pattern = '%s(.*?)%s' % (re.escape('@'), re.escape(' '))
removed_data = re.sub(pattern, '', s)
#ln=print("\n")
ln="\n" or " " or ''
pattern = '%s(.*?)%s' % (re.escape('https://t.co/'), re.escape(ln))
https_removed_data = re.sub(pattern, '\n', removed_data)
f = open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\Datapreprocessing\\noise_removed_data.txt", "w")
f.write(https_removed_data)
f.close()
print(https_removed_data)

