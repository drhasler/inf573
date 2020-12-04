import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(img):
    # img = cv2.resize(img, (0,0), fx=.5, fy=.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

"""
TODO
from filters import edges 
def segmentation(img, m)

"""
