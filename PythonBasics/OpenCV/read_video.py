#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:59:06 2023

@author: pankaj
"""

import cv2
import numpy as np
  
# Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture('video.mp4')
cap = cv2.VideoCapture(0)
# cv2.VideoCapture(0): Means first camera or webcam.
# cv2.VideoCapture(1):  Means second camera or webcam.
# cv2.VideoCapture(“file name.mp4”): Means video file
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
  
# Read until video is completed
while(cap.isOpened()):
# cap.read() returns a bool (True/False) and the image. If the frame is read correctly, it will be True. 
# Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
          
    # Press Q on keyboard to exit
    #waitKey() This number is equal to the time in milliseconds we want each frame to be displayed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break
  
# When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()