import cv2

def webcam(proc, kb={}):
    """ helper for reading video
    proc:  frame -> [ims to show], data
    kb: dict key -> func(ims,data) """
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        ims, res = proc(frame)
        for i, img in enumerate(ims):
            cv2.imshow(f'out{i}', img)

        k = cv2.waitKey(1)
        if k == -1: continue

        k = chr(k)
        if k == 'q':
            break
        if k in cb:
            cb[k](ims, res)

    cap.close()
    cv2.destroyAllWindows()

