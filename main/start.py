#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("image", help="file path to image for processing")
parser.add_argument("xml_path", help="path to XML")
parser.add_argument("-c","--cut", help="cut faces from image",
 action="store_true")
parser.add_argument("-C","--Camera", type=int, help="Camera that will capture video, default 0")

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
