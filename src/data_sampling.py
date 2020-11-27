import numpy as np
import cv2

from cv_util import cap, timed
from io_util import ...

def record(duration):
    TODO

def stills():
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

    ts = datetime.now().strftime('%Y-%m-%d')

    for l in labels:
        fname = f'{ts}:{l}.jpg'
        frame = timed(fname)
        TODO

    

