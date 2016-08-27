#Pickling
import cPickle as pickle
import os.path

def pickleClassifier(classifier):
    f=open('clssifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()
    print 'Classifier pickled successfully!!'

def loadPickled(path):
    f=open(path, 'rb')
    classifier=pickle.load(f)
    f.close()
    return classifier
    'Classifier loaded successfully!!'
    
def checkPickle(location): #make the function check for any pickle files
    if os.path.isfile(location):
        return 1
    else:
        return 0
    