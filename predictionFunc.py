#prediction function

import sklearn

final_predictions=[]

def predictionFunction(classifier, predDict):
    #for x in predDict:
    temp=predDict[0]
    final_predictions=classifier.predict(temp['text'])
    print final_predictions
    print final_predictions.shape
