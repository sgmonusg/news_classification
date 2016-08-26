#fileLoad.py
import os
from tqdm import tqdm

#class File:
    #This class describes a file.
    #Filepath
    #tags
    #bag_of_words
    #Text

files_list=[]
    
def loadFiles(root_path):
    for root in root_path:
        for a, b, files in os.walk(root):
            for x in tqdm(files):
                location=root+x
                temp_file=open(location, 'r')
                #print temp_file.read()
                temp_dict={}
                temp_dict['text']=temp_file.read()
                temp_dict['label']=str(root).strip().split('/')[-1]
                files_list.append(temp_dict)
    print len(files_list)
#file.append dict for every file
    