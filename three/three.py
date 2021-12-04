import numpy as np
import sys
import pdb

def parse_ln(numstr):
    return np.array([int(n) for n in numstr.rstrip()])

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()
    inarr = np.vstack([parse_ln(ln) for ln in lines])

# As bit columns
gamma = np.round(inarr.sum(axis=0)/inarr.shape[0]).astype(int)
epsilon = 1 - gamma

# As decimal numbers
pwr = 2**np.arange(inarr.shape[1]-1,-1,-1)
gamma = np.dot(gamma,pwr)
epsilon = np.dot(epsilon, pwr)

print("Part One")
print(gamma,epsilon,gamma*epsilon)

## Part Two

def filter_by_leading_bit(array):
    most_common = np.round(array[:,0].sum()/array.shape[0]+1e-14).astype(int)
    return most_common, np.asarray(array[:,0]==most_common)

oxygen_rating = np.zeros(inarr.shape[1],dtype=int)
CO2_rating = np.zeros(inarr.shape[1],dtype=int)

# Keep the first index so we can invert it for CO2 rating
oxygen_rating[0], first_index = filter_by_leading_bit(inarr)
ox_filter = inarr[first_index,1:]

CO2_rating[0] = 1 - oxygen_rating[0]
CO2_filter = inarr[~first_index,1:]



for i in range(1,inarr.shape[1]):
    oxygen_rating[i], ox_index = filter_by_leading_bit(ox_filter)
    ox_filter = ox_filter[ox_index,1:]

for i in range(1,inarr.shape[1]):
    if len(CO2_filter)>1:
        tmp, CO2_index = filter_by_leading_bit(CO2_filter)
        CO2_rating[i] = 1 - tmp
        CO2_filter = CO2_filter[~CO2_index,1:]
    else:
        CO2_rating[i:] = CO2_filter[0]
        break

# Convert to decimal numbers
oxygen_rating = np.dot(oxygen_rating,pwr)
CO2_rating = np.dot(CO2_rating,pwr)
life_support_rating = oxygen_rating*CO2_rating

print("Part Two")
print(oxygen_rating,CO2_rating,life_support_rating)