import sys
from heapq import heappop, heappush, merge
from collections import defaultdict
from copy import deepcopy
import numpy as np
import pdb

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()

array = np.array([[int(elem) for elem in line.rstrip()] for line in lines])

# Now we search through the array for the optimal path
def get_path_cost(array):
    maze_exit = (len(array)-1,len(array[-1])-1)

    def dist_guess(pos):
        # Return manhattan distance from this
        # pos (row,col) to the bottom-right
        # corner of the array
        return (maze_exit[0]-pos[0])+(maze_exit[1]-pos[1])

    # We will keep a heep of all the extant paths we are exploring
    pathheap = []
    init_path = ( 0 , 0, [(0,0)] ) # ( priority_cost, path_cost, list_of_path_steps)
    heappush(pathheap,init_path)
    # We will keep a mapping of the lowest path-costs found for each position
    positional_path_costs = defaultdict(lambda : np.inf)

    # Iterate until we find a working path
    while True:
        # Get the lowest estimated cost from the heap
        path_tuple = heappop(pathheap)
        _, path_cost, cur_path = path_tuple
        cur_pos = cur_path[-1]
        # If we have found the correct path, exit
        if cur_pos == maze_exit:
            break
        row, col = cur_pos
        # Otherwise, examine our neighboring nodes and add them to the heap
        neighbors = [(row+1,col), (row,col+1), (row,col-1), (row-1,col)]
        for npos in neighbors:
            # Check that the test position is a valid index
            if (npos[0] in range(0,maze_exit[0]+1)) and (npos[1] in range(0,maze_exit[1]+1)):
                # Path cost to neighbor is the cost to the current position
                # plus the cost to move into the neighbor position
                npath_cost = path_cost + array[npos[0]][npos[1]]
                # Check that our computed path cost for this neighbor is lower
                # than any pre-existing path cost for that node
                if npath_cost < positional_path_costs[npos]:
                    # This checks if our test position is in any of
                    #  the existing paths in the heap
                    if len(pathheap) > 0:
                        this_neighbor_in_search = any(npos == tup[2][-1] for tup in pathheap)
                    else:
                        this_neighbor_in_search = False
                    if not this_neighbor_in_search:
                        # Sort our heap by the total optimization cost, which is each
                        # neighbor's path cost + its heuristic cost (distance guess)
                        optimization_cost = dist_guess(npos) + npath_cost
                        npath = cur_path + [npos]
                        path_entry = (optimization_cost,npath_cost,npath)
                        positional_path_costs[npos] = path_cost
                        heappush(pathheap,path_entry)
    return path_cost, cur_path

print(get_path_cost(array)[0])
# now let's do it again but fucking bigger
def increment(ndarray):
    return np.clip((ndarray + 1)%10,a_min=1,a_max=None)
# embiggen
tmp = np.copy(array)
for i in range(4):
    tmp = increment(tmp)
    array = np.hstack([array,tmp])
tmp = np.copy(array)
for i in range(4):
    tmp = increment(tmp)
    array = np.vstack([array,tmp])

#print(array)
path_cost, long_path = get_path_cost(array)