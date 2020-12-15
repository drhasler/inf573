import numpy as np
import cv2

from loop import webcam
from dlib_face import face_features
from cv_util import draw_point
from rect_util import cen2norm
from homemade import head_direction
from visualizer import Visualizer

vis = Visualizer()
model = { "ypr": np.zeros(3) }

def process(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pts = face_features(img)

    if pts is None:
        return [img], None

    for p in pts:
        draw_point(img, *p)

    pos = (pts.mean(0) - [360,200]) / (-200);
    vis.set_pos(pos)

    ypr = model['ypr']
    alpha = .3 # change dynamically
    ypr = (1-alpha) * ypr + alpha * head_direction(pts)
    vis.look_towards(*ypr)
    model['ypr'] = ypr
    print(ypr)

    return [img], None

def status(ims, ret):
    print(ret)

if __name__ == "__main__":
    webcam(process, {'s':status} )
