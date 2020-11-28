import numpy as np
import cv2
import glob

from skimage.measure import label
from skimage.morphology import skeletonize

cap = cv2.VideoCapture(0) # cam feed
cap.set(cv2.CAP_PROP_EXPOSURE,-4)
# backSub = cv2.createBackgroundSubtractorMOG2()
ker = np.ones((15,15),np.uint8)

def mask_th(img, th=0):
    return 255 * np.uint8(img > th)

def mog(frame):
    fgm = backSub.apply(frame)
    fgm = mask_th(fgm)
    fgm = cv2.dilate(fgm, ker)
    comp = label(fgm)
    comp = np.uint8(comp)
    cmap = cv2.applyColorMap(comp, 10)
    return cmap

bgimg = None
def diff(frame):
    if bgimg is None: return frame
    d = cv2.absdiff(frame, bgimg)
    cv2.imshow('background',d)
    m = mask_th(d, 30)
    m = cv2.erode(cv2.dilate(m, ker), ker) # closing
    m = connected_comp(m)
    return m
    # skeleton = skeletonize(c)
    # return skeleton
    return frame * d

def connected_comp(mask):
    labels = label(mask)
    labels = np.uint8(labels)
    cmap = cv2.applyColorMap(labels, 2)
    x = np.argsort(np.bincount(labels.flat))
    # print(labels)
    # print(x)
    if len(x) > 2:
        return labels == x[-2]
    return labels == x[0]
    return cmap


while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out = diff(frame)

    out = 255*np.uint8(out)

    cv2.imshow('cam1', frame)
    cv2.imshow('out', out)
    # if bgimg is not None:
        
    k = cv2.waitKey(1)
    if k == ord('b'):
        bgimg = frame
    if k == ord('q'):
        break

