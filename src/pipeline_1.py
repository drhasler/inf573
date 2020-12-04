import numpy as np
import cv2

from loop import webcam
from dlib_face import face_features
from cv_util import draw_point
from rect_util import cen2norm

def process(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pts = face_features(img)

    if pts is None:
        return [img], None

    for p in pts:
        draw_point(img, *p)

    m = pts.mean(axis=0)
    m[1] -= 60 # forehead
    # r = cen2norm((*m, 10,10))
    r = cen2norm((*m, 200,10))
    # frag = img[r[1]:r[3], r[0]:r[2]]
    # report['col'] = frag.mean()

    return [img], None

def status(ims, ret):
    print(ret)

if __name__ == "__main__":
    webcam(process, {'s':status} )
