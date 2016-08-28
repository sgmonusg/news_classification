#fileLoad.py
import os
from tqdm import tqdm

#arg=1 => train set
files_list=[]
    
def loadFiles(root_path, train):
    for root in root_path:
        for a, b, files in os.walk(root):
            for x in tqdm(files):
                location=root+x
                temp_file=open(location, 'r')
                temp_dict={}
                temp_dict['text']=temp_file.read()
                if train==1:
                    temp_dict['label']=str(root).strip().split('/')[-2]
                    print 'Train data loading'
                else:
                    print 'Test data loading'
                files_list.append(temp_dict)
    print '\nAll files loaded!!'
    return files_list
    