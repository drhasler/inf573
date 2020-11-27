import numpy as np
import cv2

from np_util import sig
from cv_util import timed

def bg_diff(img, bg):
    """ masks out the background
    args:
    - img h,w uint8 col
    - bg  h,w uint8 col
    returns:
    - m1 normalized abs diff (float)
    - m2 mask (float)
    """
    m1 = cv2.absdiff(img, bg)
    m1 = m1.sum(axis=2) / (255*3)
    m2 = 1. * ( m1 > .1)

    # m1 = sig(40*(m1-.1))
    return m1, m2

def edges(img):
    """ TODO, with simple 1,-1 kernels
    arg image uint8 mono
    returns same shape """
    ...


