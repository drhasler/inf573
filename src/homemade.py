from np_util import angle

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