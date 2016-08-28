#prediction function

import sklearn

final_predictions=[]

def predictionFunction(classifier, predDict):
    print 'prediction function not yet built'
    for x in predDict:
        final_predictions.append(classifier.predict(x['text']))
    print final_predictions
