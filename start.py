#!/usr/bin/env python

import cv2 
import numpy as np
import argparse


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
  
  facesFound = faceFinder.detectMultiScale(grey,scaleFactor = 1.2,minNeighbours=10,minSize=(30,30))
  
  print("Found {} faces!".format(len(facesFound)))
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
