#!/usr/bin/env python

import cv2 
import lib as detector 
import argparse



#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("xml_path", help="path to XML")

args = parser.parse_args()

cv2.namedWindow("Face Find")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Face Find", frame)
    rval, frame = vc.read()

    frame = detector.faces(frame, args.xml_path)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Face Find")
