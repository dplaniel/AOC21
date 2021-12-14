import sys

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()

valid_dict = {")" : "(",
            "}" : "{",
            "]" : "[",
            ">" : "<"}

closing_char_dict = {"(" : ")",
                     "[" : "]",
                     "{" : "}",
                     "<" : ">"}

def find_invalid_char(line,openers=[]):
    if len(line) == 0:
        return openers
    if line[0] in ['(','[','{','<']:
        # This is an opening character
        return find_invalid_char(line[1:], openers=openers+[line[0]])
    else:
        if valid_dict[line[0]] is openers[-1]:
            return find_invalid_char(line[1:], openers=openers[:-1])
        else:
            return line[0]

part_one_scores_dict = {")" : 3,
                        "]" : 57,
                        "}" : 1197,
                        ">" : 25137
                        }

part_two_scores_dict = {")" : 1,
                        "]" : 2,
                        "}" : 3,
                        ">" : 4
                        }

# Initialize scores
part_one_score = 0
part_two_scores = []

def score_line_pt2(missing_closers):
    score = 0
    for char in missing_closers:
        score = 5*score + part_two_scores_dict[char]
    return score

for line in lines:
    # Do some puzzling
    ret_value = find_invalid_char(line.rstrip())
    if type(ret_value) is not list: # check this syntax
        part_one_score += part_one_scores_dict[ret_value]
    else:
        # Reverse openers order to get closers string
        closing_string = [closing_char_dict[char] for char in ret_value[::-1]]
        part_two_scores.append(score_line_pt2(closing_string))
        
part_two_scores.sort()
middle_val = part_two_scores[len(part_two_scores)//2]

print("Part One: ")
print(part_one_score)
print("Part Two: ")
print(middle_val)