#!/usr/bin/env python

import cv2 
import lib as detector 
import argparse

def videoCapture(xml):

	video = cv2.VideoCapture(0)
	cascade = cv2.CascadeClassifier(xml)

	while(video.isOpened()):
		returnValue, frame = video.read()

		cv2.imshow("Original", frame)
		
		facesFound = cascade.detectMultiScale(frame,1.3,5)  

  		for (x,y,w,h) in facesFound:
    			cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)

		cv2.imshow("Face Find", frame)
		key = cv2.waitKey(20)
		if key == 27: # exit on ESC
        		break
	video.release()
	cv2.destroyAllWindows()
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("xml_path", help="path to XML")

args = parser.parse_args()

try:
	open(args.xml_path, 'r')
except IOError:
	print("IoError: No such file: "+args.xml_path+" found")
	sys.exit()

videoCapture(args.xml_path)

