

def body_width(m):
    h_proj = m[-100:].sum(axis=0)
    # smooth it ?
    h_proj = (h_proj > 80).astype('int8')
    h_proj = h_proj[:-1]-h_proj[1:]
    pts = np.nonzero(h_proj)[0]
    if len(pts) < 2: return
    l = pts[0]
    r = pts[-1]
    print(r-l)