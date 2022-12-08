import glob
import os
import numpy as np
import sys
# this .py file should be in same dir as images folder(current_dir), in same path train.txt and test.txt will be created
#current_dir = "/darknet/data/yolov4_data"   #google drive folder location where imgs and annots are saved
current_dir = "yolov4_data"   # for local yolov4_data folder in same directory as this file
split_pct = 10;
file_train = open("train.txt", "w")  
file_val = open("test.txt", "w")  
counter = 1  
index_test = round(100 / split_pct)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):  
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
                counter = 1
                file_val.write(current_dir + "/" + title + '.png' + "\n")
        else:
                file_train.write(current_dir + "/" + title + '.png' + "\n")
                counter = counter + 1
file_train.close()
file_val.close()
