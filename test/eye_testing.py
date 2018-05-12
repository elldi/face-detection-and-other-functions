#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to face image")
parser.add_argument("eye_path", help="path to eyes XML")

args = parser.parse_args()

image = cv2.imread(args.image_path)
if(image is None):
	print("Image not found!")
else:
	image = lib.eyes(image, args.eye_path)

	cv2.imshow("Eyes", image)
	cv2.waitKey(0)