import numpy as np
import cv2
import dlib

from main import direct

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../data/shape_predictor_68_face_landmarks.dat')

# 45,36,54,48,30 # eyes lr, mouth lr, nose

def draw_point(frame, x, y):
    cv2.circle(frame, (int(x), int(y)), radius=0, color=(255), thickness=-1)

def draw_rect(frame, rect):
    x1,y1,x2,y2 = map(int, rect)
    cv2.rectangle(frame, (x1,y1), (x2,y2), 255, -1)

def unpack_rect(r):
    return r.left(), r.top(), r.right(), r.bottom()

def shape_array(shape, dtype=np.int):
    arr = np.zeros((68,2), dtype=np.int)
    for i in range(68):
        arr[i] = shape.part(i).x, shape.part(i).y
    return arr

def face_rect(frame):
    rects = detector(frame)
    return unpack_rect(rects[0]) if rects else None

def face_features(frame):
    """ ears lr, eyes lr, mouth lr, nose """
    rects = detector(frame)
    if not rects: return None
    pts = shape_array(predictor(frame, rects[0]))
    return pts[[16,0,45,36,54,48,30]]


