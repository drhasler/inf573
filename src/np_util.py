import numpy as np
import numpy.linalg as la

def sig(A):
    """ sigmoid activation
    A can be an array or a scalar """
    return 1/(1 + np.exp(-A))

def quant(A):
    """ 10 quantiles """
    q = np.linspace(0, 1, num=10, endpoint=True)
    return np.quantile(A, q)

def angle(a,b):
    c = np.dot(v1, v2)
    s = la.norm(np.cross(v1, v2))
    return np.arctan2(s,c)
