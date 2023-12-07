"""Appliable Functions to a Pandas GroupBy Operation (I.E Plugins)"""

import numpy as np


def tanimoto(list1, list2):
    """tanimoto coefficient

    In [2]: list2=['39229', '31995', '32015']
    In [3]: list1=['31936', '35989', '27489', '39229', '15468', '31993', '26478']
    In [4]: tanimoto(list1,list2)
    Out[4]: 0.1111111111111111

    Uses intersection of two sets to determine numerical score

    """

    intersection = set(list1).intersection(set(list2))
    return float(len(intersection)) / (len(list1) + len(list2) - len(intersection))


def npsum(x):
    """Numpy Library Sum"""

    return np.sum(x)


def npmedian(x):
    """Numpy Library Median"""

    return np.median(x)

def multiply1000(x):
    """Multipliplication by 1000"""

    return (x*1000)
    

def npround(x):
    """Numpy Library Round"""

    return np.round(x, decimals=0)
    

def npmax(x):
    """Numpy Library Median"""

    return np.max(x)


def npmean(x):
    """Numpy Library Median"""

    return np.round(np.mean(x), decimals=3)
