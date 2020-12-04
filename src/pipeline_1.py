import numpy as np
import cv2

from main import direct
from face import face_rect, face_features, draw_point, draw_rect
from edges import edges
from loop import webcam

def process(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pts = face_features(img)

    if pts is None:
        return [img], None

    for p in pts:
        draw_point(img, *p)

    # TODO make these relative values
    m = pts.mean(axis=0)
    m[1] -= 60 # forehead
    # r = normalize((*m, 10,10))
    r = normalize((*m, 200,10))
    frag = img[r[1]:r[3], r[0]:r[2]]
    # report['col'] = frag.mean()

    return [img, frag], None

def status(ims, ret):
    print(ret)

if __name__ == "__main__":
    direct(process, {'s':status} )
