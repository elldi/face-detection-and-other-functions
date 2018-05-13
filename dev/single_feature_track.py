#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib

parser = argparse.ArgumentParser()

parser.add_argument("single_path", help="path to a haar feature XML")


args = parser.parse_args()

lib.videoSingleFeature(args.single_path)