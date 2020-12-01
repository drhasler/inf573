import cv2

def direct(f, cb={}):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        res = f(frame)
        for i, img in enumerate(res):
            cv2.imshow(f'out{i}', img)

        k = cv2.waitKey(1)
        if k == -1: continue
        k = chr(k)
        if k == 'q':
            break
        if k in cb:
            cb[k](img)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--video')

    args = parser.parse_args()
    print(args)
