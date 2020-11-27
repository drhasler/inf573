import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(img):
    # img = cv2.resize(img, (0,0), fx=.5, fy=.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def body_width(m):
    h_proj = m[-100:].sum(axis=0)
    # smooth it ?
    h_proj = (h_proj > 80).astype('int8')
    h_proj = h_proj[:-1]-h_proj[1:]
    pts = np.nonzero(h_proj)[0]
    if len(pts) < 2: return
    l = pts[0]
    r = pts[-1]
    print(r-l)

"""
TODO
from filters import edges 
def segmentation(img, m)

"""
