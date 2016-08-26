import numpy as np
import hello
import fileLoad
business_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/business/'
sport_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/sport/'
tech_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/tech/'
politics_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/politics/'
entertainment_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/entertainment/'
files=[business_loc, sport_loc, tech_loc, politics_loc, entertainment_loc]

fileLoad.loadFiles(files)