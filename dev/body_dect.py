#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
    return img

'''
parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to a image")

args = parser.parse_args()


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread(args.image_path)

found,w=hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)

draw_detections(img,found)
cv2.imshow('Full body',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
video = cv2.VideoCapture(0)

while(video.isOpened()):

	returnValue, frame = video.read()
	found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)

	img = draw_detections(frame,found)

	cv2.imshow("Face Find", img)
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
video.release()
cv2.destroyAllWindows()