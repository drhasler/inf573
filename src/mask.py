import numpy as np
import cv2
from skimage.measure import label
from skimage.morphology import skeletonize

def connected_comp(img):
	""" connected components of the same color
	returns mask of second largest CC """
    labels = label(img)
    x = np.argsort(np.bincount(labels.flat))
    if len(x) > 2: return labels == x[-2]
    return labels == x[0]
    """ for one color per CC """
    labels = np.uint8(labels)
    cmap = cv2.applyColorMap(labels, 2)

# bs = cv2.createBackgroundSubtractorMOG2()
# fg_mask = bs.apply(frame)

def bg_diff(img, bg, threshold=.1):
    """ masks out the background """
    m1 = cv2.absdiff(img, bg)
    m1 = m1.sum(axis=2) / (255*3)
    m2 = 1. * ( m1 > threshold)
    
    return m1, m2

# https://en.wikipedia.org/wiki/Mathematical_morphology#Binary_morphology
# cv2.erode(), cv2.dilate()
