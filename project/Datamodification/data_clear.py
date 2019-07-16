from PyQt5.QtWidgets import QMessageBox


#This code used to clear all stored data in the files 


open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets.txt",  "w").close()
open("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\Datapreprocessing\\noise_removed_data.txt",  "w").close()

filename = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataAnalysing\\result.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()

