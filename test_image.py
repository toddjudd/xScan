#import the needed packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#init the camera and get a reference to the raw cam capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

#allow the camera to warmup and turn on
time.sleep(0.1)

#grab an image from the camera
camera.capture(rawCapture, format='bgr')
image = rawCapture.array

#display the image on screen and way for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)