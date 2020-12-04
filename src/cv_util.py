from time import time
import cv2

# cap = cv2.VideoCapture(0) # cam feed

""" cv2 cheatsheet
ret, frame = cap.read()
cv2.imread('img.jpg')
cv2.imwrite('img.jpg', img)
cv2.imshow('window', img)
cv2.destroyWindow('window')
"""

def safe_show(img):
    """ safe cast for cv2.imshow """
    if img.dtype == np.bool:
        return np.uint8(255*img)
    return img

def draw_point(frame, x, y):
    cv2.circle(frame, (int(x), int(y)), radius=0, color=(255), thickness=-1)

def draw_rect(frame, rect):
    x1,y1,x2,y2 = map(int, rect)
    cv2.rectangle(frame, (x1,y1), (x2,y2), 255, -1)

def addText(img, txt,
        origin=(50, 50),
        scale=1,
        color=(255,255,255),
        font=cv2.FONT_HERSHEY_SIMPLEX,
        thickness=2
        ):
    """ modifies the image passed """
    cv2.putText(img, txt,
        origin, font, scale,
        color, thickness, cv2.LINE_AA)


def timed(text='ready', timer=2.):
    status = 0 # waiting
    while True:
        ret, frame = cap.read()

        if status == 0:
            addText(frame, text)

        cv2.imshow('timed', frame)

        k = cv2.waitKey(1)
        if status == 0:
            if k != -1:
                t0 = time()
                status = 1
        elif status == 1:
            t = time()
            if t - t0 > timer:
                cv2.destroyWindow('timed')
                return frame

