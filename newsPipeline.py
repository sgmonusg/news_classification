#classification pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from time import time

def buildPipeline(loaded):
    text_arr=[]
    label_arr=[]
    for x in loaded:
        text_arr.append(x['text'])
        label_arr.append(x['label'])
    '''cv=CountVectorizer(decode_error='ignore')
    cv.fit_transform(text_arr)
    print 'FITTED!!'''
    pipeline=Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf',KNeighborsClassifier())])
    parameters={'vect__stop_words':['english'],'vect__decode_error':('ignore', 'replace'), 'tfidf__use_idf':(True, False), 'clf__n_neighbors':(1,2,3,4,5,6,7,8)} ###difjldjfdfkjfk
    grid_search=GridSearchCV(pipeline, parameters, verbose=4, cv=5)
    print "Performing Grid Search"
    t0=time()
    grid_search.fit(text_arr, label_arr)
    print "Time elapsed=" + str(time()-t0)+'s'
    print 'Best score' + str(grid_search.best_score_)
        
        