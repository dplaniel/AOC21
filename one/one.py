import sys
import numpy as np

infile = sys.argv[1]
with open(infile,'r') as openfile:
    numlist = [int(n) for n in openfile.readlines()]

# Part One
arr = np.array(numlist)
ct = ((arr[1:]-arr[:-1])>0).sum()

print(ct)

# Part Two
wdw = np.array([1,1,1])
cvd = np.convolve(arr,wdw,mode='valid')
ct2 = ((cvd[1:]-cvd[:-1])>0).sum()

print(ct2)