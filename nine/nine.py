import numpy as np
import sys
from scipy import ndimage

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()

array = np.array([[int(n) for n in line.rstrip()] for line in lines])
padded = np.pad(array,[[1,1],[1,1]],mode='constant',constant_values=9)

# Invoke the arcane inscriptions
# This is utterly unreadable but it's just a vectorization of 
# "Is this element smaller than its (up,down,left,right) neighbors?"
# because reasons
min_map = np.logical_and(
    np.logical_and(
        (padded[1:,1:-1]-padded[:-1,1:-1])[:-1]<0, 
        (padded[:-1,1:-1]-padded[1:,1:-1])[1:]<0
        ),
    np.logical_and(
        (padded[1:-1,1:]-padded[1:-1,:-1])[:,:-1]<0,
        (padded[1:-1,:-1]-padded[1:-1,1:])[:,1:]<0
        )
    )

print((min_map*(array+1)).sum())
# The second half is easy because somebody else already solved it lol
basins, N = ndimage.label(array!=9)
basin_sizes = [0]*N
for i in range(N):
    basin_sizes[i] = (basins==(i+1)).sum()

basin_sizes.sort(reverse=True)

print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])