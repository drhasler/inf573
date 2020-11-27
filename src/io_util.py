import os
import re

DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

files = os.listdir(DATA_DIR)
ims = [ *map(lambda fname: cv2.imread(os.path.join(DATA_DIR, fname))/255, files) ]

d = dict( zip(map(lambda s: TODO, files), ims) )
