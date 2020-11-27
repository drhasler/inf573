import numpy as np
import matplotlib.pyplot as plt
import cv2

from cv_util import timed, cap
from np_util import quant
from filters import bg_diff
from features import detect_faces, body_width

bg = timed('background')


while True:
    ret, frame = cap.read()

    m1,m2 = bg_diff(frame, bg)
    faces = detect_faces(frame)
    for (x,y,w,h) in faces:
        y -= int(h*.3)
        h = int(h*1.3)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        m2[y:y+h,x:x+w] = 0

    body_width(m2)
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

