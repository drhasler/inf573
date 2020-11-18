import numpy as np
import cv2

from skimage.measure import label

cap = cv2.VideoCapture(0) # cam feed
backSub = cv2.createBackgroundSubtractorMOG2()

ker = np.ones((5,5),np.uint8)

while True:
    ret, frame = cap.read()
    fgm = backSub.apply(frame)
    fgm = 255 * np.uint8(fgm > 0)
    fgm = cv2.dilate(fgm, ker)
    comp = label(fgm)
    comp = np.uint8(comp)
    cmap = cv2.applyColorMap(comp, 10)

    cv2.imshow('cam1', frame)
    cv2.imshow('mask', cmap)
    cv2.waitKey(1)

