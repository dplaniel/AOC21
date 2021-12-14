import sys
from copy import deepcopy

class Node(object):
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.big = name.isupper()

    def add_neighbor(self, neighbor):
        self.neighbors += [neighbor]

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()

graph = {}

for line in lines:
    a,b = line.rstrip().split("-")
    if not(a in graph.keys()):
        graph[a] = Node(a,[])
    if not(b in graph.keys()):
        graph[b] = Node(b,[])

    graph[a].add_neighbor(b)
    graph[b].add_neighbor(a)

completed_paths = []
def walk(node, path=[]):
    path.append(node.name)
    if node.name=='end':
        completed_paths.append(deepcopy(path))
    else:
        for neighbor in node.neighbors:
            # Append new current position existing paths to explore
            if (neighbor in path) and (not graph[neighbor].big):
                continue
            else:
                walk(graph[neighbor],deepcopy(path)) # the mysteries of python

def walk2(node, path=[]):
    path.append(node.name)
    visited = []
    small_cave_doubled = False
    for place in path:
        if place in visited:
            if graph[place].big is False:
                small_cave_doubled = True
        else:
            visited.append(place)

    if node.name=='end':
        completed_paths.append(deepcopy(path))
    else:
        for neighbor in node.neighbors:
            if neighbor=='start':
                continue
            # Append new current position existing paths to explore
            if not graph[neighbor].big:
                if neighbor in visited:
                    if small_cave_doubled:
                        continue
            walk2(graph[neighbor],deepcopy(path)) # the mysteries of python

walk(graph['start'],[])
for path in completed_paths:
    out_str = path[0]
    for node in path[1:]:
        out_str += "," + node
    ##print(out_str)

print(len(completed_paths))

completed_paths = []

walk2(graph['start'],[])
for path in completed_paths:
    out_str = path[0]
    for node in path[1:]:
        out_str += "," + node
    print(out_str)

print(len(completed_paths))