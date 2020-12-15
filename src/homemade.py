from np_util import angle
import numpy as np

def criss_cross(a,b,c):
    ab, ac, bc = b-a, c-a, c-b
    return angle(ab,ac), angle(ab,bc), angle(ac,bc)


def body_width(m):
	# bottom pixels
    h_proj = m[-100:].sum(axis=0)
    # most set to white
    h_proj = (h_proj > 80).astype('int8')
    # -1 1 transitions
    h_proj = h_proj[:-1]-h_proj[1:]
    pts = np.nonzero(h_proj)[0]
    if len(pts) < 2: return
    l = pts[0]
    r = pts[-1]
    print(r-l)

def head_direction(pts):
    """
    args: lr ears, nose
    returns: yaw pitch roll
    """
    lear,rear,nose = pts
    d1 = rear-lear
    d2 = nose-lear
    yaw = ( np.dot(d1,d2) / np.dot(d1,d1) - .5 ) * np.pi
    pitch = np.cross(d1,d2) / np.dot(d1,d1) * np.pi # some factor here
    roll = np.arctan2(*d1) + np.pi/2
    return np.array([
        .7*yaw, -.6-pitch, roll
    ])


