import numpy as np
import cv2

def th(img, th):
    return 1. * (img > th)

def edges(img):
    sobelx = np.abs(cv2.Sobel(img, cv2.CV_64F, 1,0))
    sobely = np.abs(cv2.Sobel(img, cv2.CV_64F, 0,1))
    return th(sobelx + sobely, .5)

if __name__ == '__main__':
    from main import direct
    direct(edges, True)
