import numpy as np
import matplotlib.pyplot as plt
import cv2

from cv_util import timed, cap
from np_util import sig, quant

bg = timed('background')
def fg_mask(img, bg):
    m1 = cv2.absdiff(frame, bg)
    m1 = m1.sum(axis=2) / (255*3)
    m2 = 1. * ( m1 > .1)

    # m1 = sig(40*(m1-.1))
    return m1, m2

face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(img):
    # img = cv2.resize(img, (0,0), fx=.5, fy=.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

while True:
    ret, frame = cap.read()

    m1,m2 = fg_mask(frame, bg)
    faces = detect_faces(frame)
    for (x,y,w,h) in faces:
        y -= int(h*.3)
        h = int(h*1.3)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        m2[y:y+h,x:x+w] = 0

    cv2.imshow('cam', frame)
    cv2.imshow('mask', m2)

    k = cv2.waitKey(1)
    if k == ord('h'):
        # print(quant(m1))
        plt.figure(1)
        plt.hist(m1.ravel(), bins=50)
        plt.figure(2)
        plt.plot(m2.sum(axis=0))
        plt.figure(3)
        plt.plot(m2.sum(axis=1))
        plt.show()
    if k == ord('b'):
        bg = timed('background')

