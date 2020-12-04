
def rect2norm(r):
    """ from dlib rect to normal """
    return r.left(), r.top(), r.right(), r.bottom()

def cen2norm(r):
    """ from normal to centered """
    cx = (r[0]+r[2])/2
    dx = (r[2]-r[0])/2
    cy = (r[1]+r[3])/2
    dy = (r[3]-r[1])/2
    return (cx, cy, dx, dy)

def norm2cen(r):
    """ from centered to normal """
    cx,cy,dx,dy = r
    return cx-dx, cy-dy, cx+dx, cy+dy
