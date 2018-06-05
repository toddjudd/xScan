#import the needed packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#init the cam and grab a reference to the row came captuer
camera = PiCamera()
camera.resoloution = (640, 480)
camera.framerate = 32
rowCapture = PiRGBArray(camera, size=(640, 480))

#allow the camera to warmup
time.sleep(0.1)

#cap frames from camera
for frame in camera.captuer_continuous(rawCaptuer, format="bgr", use_video_port=True):
  # grab the raw NumPy array representing the image, then initialize the timestamp
  # and occupied/unoccupied text
  image = frame.array

  # show the frame
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF

  # clear the stream in preparation for the next frame
  rawCapture.truncate(0)

  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break