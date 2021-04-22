import numpy as np
import matplotlib.pyplot as plt

# The following helper functions simplify the SPEIS data import from MPT files


def get_boundaries(highest_freq, lowest_freq, f):
    if (np.count_nonzero(f[0] >= highest_freq) > 0):
        cutoff_start = np.where(f[0] >= highest_freq)[0][-1]
    else:
        cutoff_start = 0
    if (np.count_nonzero(f[0] <= lowest_freq) > 0):
        cutoff_end = np.where(f[0] <= lowest_freq)[0][0]
    else:
        cutoff_end = len(f[0])-1
    return cutoff_start, cutoff_end