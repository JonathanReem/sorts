import numpy as np

def np_sort(unsorted):
    unsorted = np.asarray(unsorted)
    s = np.repeat(np.arange(1+unsorted.max()), np.bincount(unsorted))
    return s.tolist()

def simple_np_sort(a):
    a = np.asarray(a)
    s = a.sort()
    return a.tolist()