#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:59:06 2023

@author: pankaj
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0 )  # capture video from file
# cap = cv2.VideoCapture(0)  # capture video from web-cam

if cap.isOpened() == False:
    print("Unable to read camera feed!")

frame_width = int(cap.get(3)) #cv2.CAP_PROP_FRAME_WIDTH
frame_height = int(cap.get(4)) #cv2.CAP_PROP_FRAME_HEIGHT
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #7
print(frame_width)
print(frame_height)
print(frame_count)

# The arguments used in cv2.VideoWriter(const String &  filename,
#                                       int     fourcc,
#                                       double  fps,
#                                       Size    frameSize,
#                                       bool    isColor = true):
# filename  Name of the output video file.
# fourcc    4-character code of codec used to compress the frames.
#           In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
#           In Windows: DIVX (More to be tested and added)
#           In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).
# fps   Framerate of the created video stream.
# frameSize Size of the video frames.
# isColor   If it is not zero, the encoder will expect and encode color frames, otherwise it will work with grayscale frames 
#         (the flag is currently supported on Windows only).

out = cv2.VideoWriter('my_cam.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
     25, 
    (frame_width,frame_height), isColor=1)

i = 0 
while (cap.isOpened()  ):
    ret, frame = cap.read()

    if ret == True:
      i = i + 1
      cv2.imshow('Frame', frame)
      # write the images to video file
      out.write(frame)
      
      
      
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
      break

cap.release()
out.release()

cv2.destroyAllWindows()