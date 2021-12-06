import numpy as np

with open("input_five.txt",'r') as openfile:
    lines = openfile.readlines()


segments = []
max_x = 1
max_y = 1

for line in lines:
    start, end = line.rstrip().split(" -> ")
    x1,y1 = [int(x) for x in start.split(",")]
    x2,y2 = [int(x) for x in end.split(",")]
    # No diagonals allowed in this part of town
    if (x1 != x2) and (y1 != y2):
        continue

    max_x = max(max_x,x1,x2)
    max_y = max(max_y,y1,y2)

    segments.append((x1,y1,x2,y2))

grid = np.zeros([max_x+2,max_y+2],dtype=int)

for segment in segments:
    (x1,y1,x2,y2) = segment
    if x1==x2:
        lo = min(y1,y2)
        hi = max(y1,y2) + 1
        grid[x1,lo:hi] += 1
    else:
        lo = min(x1,x2)
        hi = max(x1,x2) + 1
        grid[lo:hi,y1] += 1

print("Part One")
print((grid>1).sum())


segments = []
for line in lines:
    start, end = line.rstrip().split(" -> ")
    x1,y1 = [int(x) for x in start.split(",")]
    x2,y2 = [int(x) for x in end.split(",")]
    # No diagonals allowed in this part of town
    if (x1 == x2) or (y1 == y2):
        continue

    max_x = max(max_x,x1,x2)
    max_y = max(max_y,y1,y2)

    segments.append((x1,y1,x2,y2))

# Part Two
print("Part Two")

for segment in segments:
    (x1,y1,x2,y2) = segment

    if x2 > x1:
        xstep = 1
    else:
        xstep = -1
    if y2 > y1:
        ystep = 1
    else:
        ystep = -1

    y = y1
    for x in range(x1,x2+xstep,xstep):
        grid[x,y] += 1
        y += ystep

print((grid>1).sum())