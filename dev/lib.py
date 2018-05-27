#!/usr/bin/env python

import cv2 

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------
def faces(image, cascadePath):

  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faceFinder = cv2.CascadeClassifier(cascadePath)
  
  facesFound = faceFinder.detectMultiScale(grey,1.3,5)  

  for (x,y,w,h)in facesFound:
    cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)

  return image

def eyes(image, cascadePath):

	grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	eyeFinder = cv2.CascadeClassifier(cascadePath)
	eyes = eyeFinder.detectMultiScale(grey)

	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(image, (ex,ey),(ex+ew, ey+eh), (255,0,0), 2)

	return image



def video(facePath, eyePath):

	video = cv2.VideoCapture(0)
	faceCascade = cv2.CascadeClassifier(facePath)
	eyeCascade = cv2.CascadeClassifier(eyePath)

	colorCutFace = 0  

	while(video.isOpened()):
		returnValue, frame = video.read()

		greyFace = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		facesFound = faceCascade.detectMultiScale(greyFace,1.3,5)
 

  		for (x,y,w,h) in facesFound:
  			cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)

			cutFace = greyFace[y:y+h, x:x+w]
			colorCutFace = frame[y:y+h, x:x+w]
			eyes = eyeCascade.detectMultiScale(cutFace)

			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(colorCutFace, (ex,ey),(ex+ew, ey+eh), (255,0,0), 2)



		cv2.imshow("Face Find", frame)
		key = cv2.waitKey(20)
		if key == 27: # exit on ESC
			break
	video.release()
	cv2.destroyAllWindows()

def videoSingleFeature(eye):
	video = cv2.VideoCapture(0)

	eyeCascade = cv2.CascadeClassifier(eye)

	while(video.isOpened()):
		returnValue, frame = video.read()
		greyFace = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
		eyeFound = eyeCascade.detectMultiScale(greyFace,1.3,5)

		for (x,y,w,h) in eyeFound:
			cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)

		cv2.imshow("Single Feature Find", frame)
		key = cv2.waitKey(20)
		if key == 27: # exit on ESC
			break

	video.release()
	cv2.destroyAllWindows()













