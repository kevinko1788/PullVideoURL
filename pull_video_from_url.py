import cv2
import numpy as np
import os
import urllib.request


# commented lines are for future use
# 1. saves video from the link to /video
# 2. extracts frame by frame saves to /video_frame
def store_raw_video():
    # change below URL as needed
    video_link = "https://pastebin.com/raw/H6vgQWk9"
    video_link_urls = urllib.request.urlopen(video_link).read().decode()
    
    if not os.path.exists('video'):
        os.makedirs('video')
#     if not os.path.exists('_video'):
#         os.makedirs('_video')    
    if not os.path.exists('video_frame'):
        os.makedirs('video_frame')
    
    video_num = 1
    
    for i in video_link_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "video/"+str(video_num)+".mp4")
            cap = cv2.VideoCapture("video/"+str(video_num)+".mp4")
#             fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#             out = cv2.VideoWriter("_video/"+str(video_num)+".mp4")
            ret, frame = cap.read()
            while ret:

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 resize_image = cv2.resize(gray, (100,100))
                cv2.imwrite("video_frame/"+str(video_num)+".jpg",gray)
#                 out.write(frame)
                ret, frame = cap.read()
                video_num+=1
            
        except Exception as e:
            print(str(e))

store_raw_video()