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
    
def read_mpt_parameters(filename):
    with open(filename, 'r', encoding="latin-1") as input_file:
        lines = input_file.readlines()
    header_line = lines[1]
    header_lines_number = int(header_line.split(":")[1])
    
    # Iterate over headline section containing relevant information
    for i in range(header_lines_number):
        if lines[i].startswith("Ei (V)"):
            pot_start = float(lines[i].split("(V)")[1])*1E+3
        if lines[i].startswith("Ef (V)"):
            pot_end = float(lines[i].split("(V)")[1])*1E+3
        if lines[i].startswith("N"):
            potstepnumber = int(lines[i].strip().split(" ")[-1])+1
    pot_step = int(abs(pot_start-pot_end)/(potstepnumber-1))
    return pot_start, pot_step, potstepnumber