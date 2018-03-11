#!/usr/bin/env python

import cv2 
import numpy as np
import sys


#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
imageScan = sys.argv[1] #'C:/Users/Adams/Desktop/faces.jpg'
cascadePath = sys.argv[2]#'C:/Users/Adams/Desktop/ee.xml'

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------
def Faces():
  image = cv2.imread(imageScan)
  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  faceFinder = cv2.CascadeClassifier(cascadePath)
  
  cv2.imshow("Original" ,image)
  cv2.imshow("Grey" ,grey)
  
  facesFound = faceFinder.detectMultiScale(grey,1.3,5)  
  print("Found {} faces!".format(len(facesFound)))

  for (x,y,w,h)in facesFound:
	cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)
  cv2.imshow("Faces found",image)
  cv2.waitKey(0)
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
Faces()
