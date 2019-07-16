import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import subprocess
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'predicta interface'
        self.left = 10
        self.top = 60
        self.width = 520
        self.height = 600
        self.initUI()
        self.layout = QVBoxLayout()
        self.label = QLabel("My text")

      
        
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        #predicta title

        label = QLabel("PREDICTA", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("QLabel {color: rgb(58, 78, 155);font: 30pt ;font-weight: bold;font-family:serif;}")
        label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        label.move(160,50)



        #data analysing part
        
        label = QLabel("* DATA ANALYSING", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("QLabel {color: black;font: 10pt ;font-weight: bold;}")
        label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        label.move(60,150)
        #label.setStyleSheet("QLabel {font: 10pt }")
        
        
        button = QPushButton('RESULT HISTORY', self)
        button.setToolTip('This is an example button')
        button.move(100,230)
        button.resize(150,20)
        button.setStyleSheet("background-color:rgb(206, 160, 99)");
        button.clicked.connect(self.on_click_result_history)

        button = QPushButton('ANALYSE LATEST RESULT', self)
        button.setToolTip('This is an example button')
        button.move(100,190)
        button.resize(150,20)
        button.setStyleSheet("background-color:rgb(55,200,0)");
        button.clicked.connect(self.on_click_latest_result)

        #set dta preprocessing part

        label = QLabel("* PREPROCESSING", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("QLabel {color: black;font: 10pt ;font-weight: bold;}")
        label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        label.move(60,280)
        
        
        
        button = QPushButton('DATA PREPROCESSING', self)
        button.setToolTip('This can preprocess the stored data in file..')
        button.move(100,310)
        button.resize(150,20)
        button.setStyleSheet("background-color:rgb(141, 206, 99)");
        button.clicked.connect(self.on_click_preprocessing)

        #data extraction

        label = QLabel("* DATA EXTRACTION ", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("QLabel {color: black;font: 10pt ;font-weight: bold;}")
        label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        label.move(60,350)
    
        
        
        button = QPushButton('TWEETS IN PARTICULAR LOCATION', self)
        button.setToolTip('This button extract tweets with specific key in specific location')
        button.move(100,390)
        button.resize(200,20)
        button.setStyleSheet("background-color:rgb(157, 125, 160)");
        button.clicked.connect(self.on_click_particular_location)

        button = QPushButton('EXTRACT PARTICULAR TWEETS', self)
        button.setToolTip('This button extract some specific tweets with id')
        button.move(100,420)
        button.resize(200,20)
        button.setStyleSheet("background-color:rgb(55,200,0)");
        button.clicked.connect(self.on_click_specific_tweets)

        button = QPushButton('EXTRACT TWEETS OF A USER', self)
        button.setToolTip('This button extract some specific tweets of particular user with user ids')
        button.move(100,450)
        button.resize(200,20)
        button.setStyleSheet("background-color:rgb(155,100,59)");
        button.clicked.connect(self.on_click_specific_user_tweets)

        button = QPushButton('EXTRACT KEYWORD TWEETS', self)
        button.setToolTip('This button extract some specific tweets of particular user with given keywords')
        button.move(100,480)
        button.resize(200,20)
        button.setStyleSheet("background-color:rgb(122, 130, 119)");
        button.clicked.connect(self.on_click_specific_keyword_tweets)



        

        button = QPushButton('CLEAR ENTIRE EXTRACTED DATA', self)
        button.setToolTip('This button extract some specific tweets of particular user with user ids')
        button.move(100,510)
        button.resize(200,20)
        button.setStyleSheet("background-color:rgb(66, 244, 209)");
        button.clicked.connect(self.on_click_clear_data)




        label = QLabel("* EXPERT OPTION", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("QLabel {color: black;font: 10pt ;font-weight: bold;}")
        label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        label.move(340,350)

        button = QPushButton('MODIFY DATA MODEL', self)
        button.setToolTip('This button extract some specific tweets of particular user with user ids')
        button.move(380,390)
        button.setStyleSheet("background-color:rgb(155,100,159)");
        button.clicked.connect(self.on_click_modify_data_model)



        
        
        self.show()

        
       
        
    


    @pyqtSlot()
    def on_click_result_history(self):
        subprocess.call(['python', 'result_history.py'])
    @pyqtSlot()
    def on_click_latest_result(self):
        subprocess.call(['python', 'naive_bayes.py'])
        
    @pyqtSlot()
    def on_click_preprocessing(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\Datapreprocessing\\removal_of_@_in_string.py'])
        QMessageBox.about(self, "Title", " Preprocessing of stored data are completed....")

    @pyqtSlot()
    def on_click_particular_location(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\tweets_in_particular_location.py'])

    @pyqtSlot()
    def on_click_specific_tweets(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\extraction_of_particular_tweet.py'])                   

    @pyqtSlot()
    def on_click_specific_user_tweets(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\twitter_perticular_user_tweets_streaming.py'])                   


    @pyqtSlot()
    def on_click_specific_keyword_tweets(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\DataExtraction\\twitter_stream_only_text.py'])                   


    @pyqtSlot()
    def on_click_clear_data(self):
        subprocess.call(['python', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\Datamodification\\data_clear.py'])                   
        QMessageBox.about(self, "Successful", " Stored data are cleared....")


    @pyqtSlot()
    def on_click_modify_data_model(self):
        QMessageBox.about(self, "Alert", "The data modification must obey the modification manual. Otherwise it may lead to run time error.")
        subprocess.call(['python', 'data_model_modification.py'])                   
        





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
