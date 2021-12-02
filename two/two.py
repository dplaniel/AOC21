import sys

with open(sys.argv[1],'r') as infile:
    commands = infile.readlines()

## Part One
X, Y = (0, 0)

for command in commands:
    dirn, step = command.split(" ")
    if dirn == "forward":
        X += int(step)
    elif dirn == "down":
        Y += int(step)
    elif dirn == "up":
        Y = max(Y-int(step),0)
    else:
        "Did not recognize command: {}".format(command)
print("Part one")
print(X, Y, X*Y)

## part Two
aim = 0
X, Y = (0, 0)

for command in commands:
    dirn, step = command.split(" ")
    if dirn == "forward":
        X += int(step)
        Y = max(Y+aim*int(step),0)
    elif dirn == "down":
        aim += int(step)
    elif dirn == "up":
        aim -= int(step)
    else:
        "Did not recognize command: {}".format(command)

print("Part Two")
print(X, Y, X*Y)