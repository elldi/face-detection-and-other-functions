#!/usr/bin/env python

import cv2 
import numpy as np
import argparse


#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
imageScan = sys.argv[1]
cascadePath = sys.argv[2]

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------
def Faces():
  image = cv2.imread(imageScan)
  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  faceFinder = cv2.CascadeClassifier(cascadePath)
  
  cv2.imshow("Original" ,image)
  cv2.imshow("Grey" ,grey)
  
  facesFound = faceFinder.detectMultiScale(grey,scaleFactor = 1.2,minNeighbours=10,minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
  
  print("Found {} faces!".format(len(facesFound)))
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
