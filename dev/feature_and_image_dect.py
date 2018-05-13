#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib

parser = argparse.ArgumentParser()

parser.add_argument("single_path", help="path to a haar feature XML")
parser.add_argument("image_path", help="path to a image")


args = parser.parse_args()

img = cv2.imread(args.image_path)

output = lib.eyes(img, args.single_path)

cv2.imshow('Full body',output)
cv2.waitKey(0)
cv2.destroyAllWindows()