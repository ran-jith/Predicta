import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
print(ss)
