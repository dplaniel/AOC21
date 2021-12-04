import numpy as np
import sys
import pdb
import re

# Open file and read lines
with open("input_four.txt", 'r') as infile:
    numline = infile.readline().rstrip()
    numlist = [int(x) for x in numline.split(",")]
    
    _ = infile.readline()

    all_lines = infile.readlines()

# Set up array of arrays
arrays = np.zeros((1,5,5),dtype=int)
array_idx = 0
line_idx = 0

# Iterate through our read lines
for i, line in enumerate(all_lines):
    # When we hit a line break, create new block
    if line == "\n":
        array_idx += 1
        line_idx = 0
        array = np.zeros((1,5,5),dtype=int)
        arrays = np.vstack([arrays,array])
    # Otherwise add new lines to existing block
    else:
        splits = re.split("\s+",line.lstrip().rstrip())
        try:
            arrays[array_idx,line_idx] = [int(x) for x in splits]
        except Exception as e:
            print(e)
            pdb.set_trace()
        line_idx += 1

# Create sets from the rows and columns of each card
list_of_bingo_sets = []
for array in arrays:
    row_sets = [set(tuple(row)) for row in array]
    col_sets = [set(tuple(col)) for col in array.T]
    list_of_bingo_sets.append(row_sets+col_sets)

first = None
matched = []
# Now iterate through number calls
for k in range(4,len(numlist)):
    called_set = set(tuple(numlist[:k+1]))
    # Check each bingo card
    for n, bingo_set in enumerate(list_of_bingo_sets):
        if n in matched:
            continue
        # Check each row and column in each bingo card
        for rowcol_set in bingo_set:
            if len(called_set.intersection(rowcol_set)) == 5:
                if first is None:
                    first = (n,k)
                latest = (n,k)
                matched.append(n)

# now score our cards
# Part One - winner
print("Part One")
n,k = first
winner = arrays[n]
called_set = set(tuple(numlist[:k+1]))
card_set = set(tuple(winner.flatten()))
out_nums = card_set.difference(called_set)
score = sum(out_nums) * numlist[k]
print("Card {}, score: {}".format(n,score))
print(arrays[n])
print("Last number called: {}".format(numlist[k]))

# Part Two - guaranteed loser
print("Part Two")
n,k = latest
winner = arrays[n]
called_set = set(tuple(numlist[:k+1]))
card_set = set(tuple(winner.flatten()))
out_nums = card_set.difference(called_set)
score = sum(out_nums) * numlist[k]
print("Card {}, score: {}".format(n,score))
print(arrays[n])
print("Last number called: {}".format(numlist[k]))
