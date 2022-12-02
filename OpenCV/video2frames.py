import cv2
v1 = "video1.mp4"

vidObj = cv2.VideoCapture(v1)
count = 0
success = 1
output_path = "/frames/"
while success:
    vidObj.set(cv2.CAP_PROP_POS_MSEC,(count*1000))  ### 1 frame/sec
    success, image = vidObj.read()
    cv2.imwrite("video1frame%d.jpg" % count, image)
    count += 1
    
    
