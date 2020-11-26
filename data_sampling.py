from datetime import datetime
from time import time
import os

import numpy as np
import cv2

DATA_DIR = 'data'

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

os.makedirs(DATA_DIR, exist_ok=True)
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

    status = 'wait'
    while 1:
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pre = img.copy()

        if status == 'wait':
            addText(pre, fname)
        else:
            t = time()
            addText(pre, str(dt-(t-t0))[:4])

        cv2.imshow('preview', pre)
        k = cv2.waitKey(1)

        if status == 'wait':
            if k != -1:
                status = 'timer'
                t0 = time()
        else:
            if t-t0 > dt:
                cv2.imshow('output', img)
                # write to data
                cv2.imwrite(os.path.join(DATA_DIR, fname), img)
                break

