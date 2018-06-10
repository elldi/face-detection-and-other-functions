#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib
import os


def draw_detections(img, rects, color):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), color, 2)
    return img 
def draw_face(img, rects, color):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(w*1.15), int(h*1.05)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), color, 2)
    return img 

parser = argparse.ArgumentParser()

parser.add_argument("video_path", help="path to video")
parser.add_argument("face_path", help="path to face XML")


args = parser.parse_args()

video = cv2.VideoCapture(args.video_path)
faceCascade = cv2.CascadeClassifier(args.face_path)

colorCutFace = 0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 20, (800,450), True)

total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

counter = 0

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while(video.isOpened()):

	ret, frame = video.read()

	if(ret == False or counter > total):
		break

	greyFace = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	facesFound = faceCascade.detectMultiScale(greyFace,1.3,5)

	found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)

	img = draw_detections(frame,found, (0,255,0))

	img = draw_face(img,facesFound, (0,0,255))

	resized_image = cv2.resize(img, (800, 450)) 
	out.write(resized_image)
	counter += 1

	sys.stdout.write("Processing frames: %d / %d    \r" % (counter, total))
	sys.stdout.flush()

video.release()
out.release()
os.system('clear')

os.system('say "completed processing"')




