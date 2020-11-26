import numpy as np

def sig(A):
    """ sigmoid activation
    A can be an array or a scalar """
    return 1/(1 + np.exp(-A))

def quant(A):
    q = np.linspace(0, 1, num=10, endpoint=True)
    return np.quantile(A, q)


