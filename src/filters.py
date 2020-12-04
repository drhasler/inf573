import numpy as np
import cv2

from np_util import sig
from cv_util import timed

def edges(img):
    """ ... """
    sobelx = np.abs(cv2.Sobel(img, cv2.CV_64F, 1, 0))
    sobely = np.abs(cv2.Sobel(img, cv2.CV_64F, 0, 1))
    return th(sobelx + sobely, .5)


