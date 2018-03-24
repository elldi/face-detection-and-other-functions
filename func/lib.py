#!/usr/bin/env python

import cv2 

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------
def faces(image, cascadePath):

  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faceFinder = cv2.CascadeClassifier(cascadePath)
  
  facesFound = faceFinder.detectMultiScale(grey,1.3,5)  

  for (x,y,w,h)in facesFound:
    cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)

  return image