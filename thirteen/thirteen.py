import sys
import numpy as np

pairs = []
folds = []
with open(sys.argv[1],'r') as infile:
    for line in infile.readlines():
        if line=="\n":
            continue
        if line.startswith("f"):
            eqn = line.rstrip().split(" ")[2]
            dir,amt = eqn.split("=")
            folds.append((dir,int(amt)))

        else:
            x,y = line.rstrip().split(",")
            pairs.append((int(x),int(y)))

xs = [x for (x,y) in pairs]
ys = [y for (x,y) in pairs]

array = np.zeros([max(xs)+1,max(ys)+1],dtype=bool) # Thank you, Steve

for (x,y) in pairs:
    array[x,y] = True
import pdb
for fold in folds:
    #pdb.set_trace()
    if fold[0]=='x':
        xval = fold[1]
        r = (array.shape[0]-1) - xval
        if r == xval:
            array = array[:xval] + array[xval+1:][::-1]
        elif r > xval:
            array = np.pad(array[:xval],[[r-xval,0],[0,0]],'constant') + array[xval+1:][::-1]
        else:
            array = array[:xval] = np.pad(array[xval+1:],[[0,xval-r],[0,0]],'constant')[::-1]
    else:
        yval = fold[1]
        r = (array.shape[1]-1) - yval
        if r == yval:
            array = array[:,:yval] + array[:,yval+1:][:,::-1]
        elif r > yval:
            array = np.pad(array[:,:yval],[[0,0],[r-yval,0]],'constant') + array[:,yval+1:][:,::-1]
        else:
            array = array[:,:yval] + np.pad(array[:,yval+1:],[[0,0],[0,yval-r]],'constant')[:,::-1]

def writenum(num):
    if num==0:
        return "."
    else:
        return "#"

print(array.sum())
for row in array.T:
    ln = ""
    for char in row:
        ln += writenum(char)
    print(ln)