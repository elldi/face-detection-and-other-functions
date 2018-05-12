#!/usr/bin/env python

import cv2 
import numpy as np
import sys
import argparse
import lib

parser = argparse.ArgumentParser()

parser.add_argument("eye_path", help="path to eyes XML")


args = parser.parse_args()

lib.videoSingleFeature(args.eye_path)