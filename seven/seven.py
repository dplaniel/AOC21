import numpy as np
import sys

with open(sys.argv[1],'r') as infile:
    line = infile.readline().rstrip()

pos = np.array([int(x) for x in line.split(",")],dtype=int)
avg = np.median(pos)
cost = np.abs(pos-avg).sum().astype(int)
print(cost)

avg = pos.mean()
p1 = np.abs(pos-np.round(avg-0.5))
p2 = np.abs(pos-np.round(avg+0.5))
def cost(p): 
    return (0.5*p*(p+1)).sum().astype(int)
print(min(cost(p1),cost(p2)))