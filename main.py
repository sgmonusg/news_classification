import numpy as np
#import hello
#   import fileLoad
from sklearn.feature_extraction.text import CountVectorizer
business_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/business/'
sport_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/sport/'
tech_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/tech/'
politics_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/politics/'
entertainment_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/entertainment/'
files=[business_loc, sport_loc, tech_loc, politics_loc, entertainment_loc]

openfil1=open(business_loc+str('001.txt') , 'r')
openfil2=open(business_loc+str('002.txt') , 'r')
openfil3=open(business_loc+str('003.txt') , 'r')
string1=openfil1.read()
string2=openfil2.read()
string3=openfil3.read()
l=[string1, string2, string3]
cv=CountVectorizer()
bow=cv.fit_transform(l)
print bow
#fileLoad.loadFiles(files)