import numpy as np
import cv2

from cv_util import timed
from io_util import ...

labels = [
  'background',
  '90_left',
  '60_left',
  '30_left',
  'front',
  '30_right',
  '60_right',
  '90_right',
  *map(lambda i: f'sample{i:03d}', range(10))
]

cap = cv2.VideoCapture(0) # cam feed
cap.set(cv2.CAP_PROP_EXPOSURE,-4) # v4lucp on linux

dt = 2. # timer, in seconds
ts = datetime.now().strftime('%Y-%m-%d')

def addText(img, txt):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, txt,
        (100, 50), font, 1, # origin, font, scale
        (255, 255, 255), 2, cv2.LINE_AA) # color, thickness

for l in labels:
    fname = f'{ts}:{l}.jpg'
    frame = timed(fname)
    TODO

    

