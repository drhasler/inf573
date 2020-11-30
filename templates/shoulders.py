import numpy as np
import cv2

from main import direct
from face import face_rect, face_features, draw_point, draw_rect
from edges import edges

def centered_rect(r):
    cx = (r[0]+r[2])/2
    dx = (r[2]-r[0])/2
    cy = (r[1]+r[3])/2
    dy = (r[3]-r[1])/2
    return (cx, cy, dx, dy)

def normalize(r):
    cx,cy,dx,dy = r
    return tuple(map(int,(cx-dx, cy-dy, cx+dx, cy+dy)))

report = {}

def process(img):
    global report

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pts = face_features(img)

    # img = edges(img/255)
    if pts is None:
        return [img]

    for p in pts:
        draw_point(img, *p)

    # TODO make these relative values
    m = pts.mean(axis=0)
    m[1] -= 60 # forehead
    # r = normalize((*m, 10,10))
    r = normalize((*m, 200,10))
    frag = img[r[1]:r[3], r[0]:r[2]]
    report['col'] = frag.mean()

    return [img, frag]

def status(img):
    print(report['col'])

if __name__ == "__main__":
    direct(process, {'s':status} )
