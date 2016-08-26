import numpy as np
import pandas as pd
import sklearn
import os
from tqdm import tqdm

business_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/business/'
sport_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/sport/'
tech_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/tech/'
politics_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/politics/'
entertainment_loc='/home/shubham/Desktop_files/news_classification/news-sort-master/Different-news-articles-classified-master/Training set/entertainment/'

word_dict={}
doc_dict={}

for root, subdir, fil in os.walk(business_loc):
    for x in tqdm(fil):
        loc=business_loc+str(x)
        buff=open(loc, 'r')
        for line in buff:
            words=line.lower().strip().split(' ')
            for word in words:
                if word not in word_dict.keys():
                    word_dict[word]=0
                    doc_dict[word]=[]
                word_dict[word]=word_dict[word]+1   
            
                doc_dict[word].append(word_dict[word])
    
        
print doc_dict