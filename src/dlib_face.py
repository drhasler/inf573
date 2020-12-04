import numpy as np
import dlib

from dlib_util import *

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../data/shape_predictor_68_face_landmarks.dat')

def shape_array(shape, dtype=np.int):
    """ dlib face features """
    arr = np.zeros((68,2), dtype)
    for i in range(68):
        arr[i] = shape.part(i).x, shape.part(i).y
    return arr

def face_features(img):
    """ ears lr, eyes lr, mouth lr, nose """
    rects = detector(frame)
    if not rects: return None
    pts = shape_array(predictor(frame, rects[0]))
    return pts[[16,0,45,36,54,48,30]]
