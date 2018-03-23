#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse


#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------
def faces(imageScan, cascadePath, toCut):

  image = cv2.imread(imageScan)
  if(image is None):
    print("Image not found!")
    return 0

  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faceFinder = cv2.CascadeClassifier(cascadePath)

  # cv2.imshow("Original" ,image)
  # cv2.imshow("Grey" ,grey)
  
  facesFound = faceFinder.detectMultiScale(grey,1.3,5)  
  print("Found {} faces!".format(len(facesFound)))

  for (x,y,w,h)in facesFound:
    cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)

    if(toCut):
      cutImage = image[y:y+h, x: x+w]
      cv2.imshow("Faces found",cutImage)
      cv2.waitKey(0)
    
  cv2.imshow("Faces found",image)
  cv2.waitKey(0)

def videoCapture(xml, camera):

	video = cv2.VideoCapture(camera)
	cascade = cv2.CascadeClassifier(xml)

	while(video.isOpened()):
		returnValue, frame = video.read()

		cv2.imshow("Original", frame)
		
		facesFound = cascade.detectMultiScale(frame,1.3,5)  

  		print("Found {} faces!".format(len(facesFound)))

  		for (x,y,w,h) in facesFound:
    			cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)

		cv2.imshow("Face Find", frame)

		if key == 27: # exit on ESC
        		break
	video.release()
	cv2.destroyAllWindows()
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("image", help="file path to image for processing")
parser.add_argument("xml_path", help="path to XML")
parser.add_argument("-c","--cut", help="cut faces from image",
 action="store_true")
parse.add_argument("-C","--Camera", type=int, help="Camera that will capture video, default 0")

args = parser.parse_args()

try:
    open(args.xml_path, 'r')
except IOError:
    print("IOError: No such file XML: '" + args.xml_path + "'")
    sys.exit()


faces(args.image, args.xml_path, args.cut)

if args.camera != 0:
	videoCapture(args.xml_path, args.camera)
else:	
	videoCapture(args.xml_path, 0)
