
#1
from moviepy.editor import *
import cv2

#list of images -> os.listdir()
images = ['image10-11.jpeg', 'image10-15.jpeg', 'image10-5.jpeg', 'image10-8.jpeg', 'image3-1.jpeg', 'image3-15.jpeg', 'image3-3.jpeg', 'image3-4.jpeg', 'image5-5.jpeg', 'image5-6.jpeg', 'Screenshot 2022-11-29 175434.jpeg', 'Screenshot 2022-11-29 175459.jpeg']

#resizing all to 1 shape, moviepy wont work with diff shapes
for img in images:
    i = cv2.imread(img)
    i = cv2.resize(i,(640,480))
    cv2.imwrite(img,i)
    #images2.append[i]

# creating a Image sequence clip with fps = 1
clip = ImageSequenceClip(images, fps = 1)
clip.write_videofile("myvideo.mp4", fps=1)
# showing  clip 
#clip.ipython_display(width = 360) 



#2
import cv2
import numpy as np
import glob
import moviepy.editor as moviepy
import os

frameSize = (500, 500)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

for filename in glob.glob('C:/Users/punam.anil.naik/Downloads/nfs/*.jpeg'):
    img = cv2.imread(filename)
    out.write(img)

clip = moviepy.VideoFileClip('output_video.avi')
clip.write_videofile("myvideo.mp4", fps=1)

out.release()


#3
import os
import glob
from natsort import natsorted
from moviepy.editor import *

base_dir = os.path.realpath("C:/Users/punam.anil.naik/Downloads/nfs")
print(base_dir)

#gif_name = 'pic'
#fps = 24

file_list = glob.glob('*.jpeg')  # Get all the pngs in the current directory
file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images

clips = [ImageClip(m).set_duration(1)
         for m in file_list_sorted]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=1)
