import sys

with open("input_six.txt",'r') as infile:
    line = infile.readline()

fish_pop_list = [0,0,0,0,0,0,0,0,0]

for fish_age in line.rstrip().split(","):
    fish_pop_list[int(fish_age)] += 1

print(fish_pop_list)

for day in range(int(sys.argv[1])):
    births = fish_pop_list[0]
    fish_pop_list[:-1] = fish_pop_list[1:]
    # Newborn fish originate with 9 days to birth
    fish_pop_list[8] = births
    # Parent fish will birth again in 7 days
    fish_pop_list[6] += births

print(fish_pop_list)
print(sum(fish_pop_list))