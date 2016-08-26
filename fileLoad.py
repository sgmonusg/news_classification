#fileLoad.py
import os

class File:
    #This class describes a file.
    #Filepath
    #tags
    #bag_of_words
    #Text

files=[]
    
def loadFiles(root_path):
    for root in root_path:
        for a, b, files in os.walk(root):
            
        
        #file.append dict for every file
    