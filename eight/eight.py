with open("input_eight.txt",'r') as infile:
    lines = infile.readlines()

part_one_answer = 0
part_two_answer = 0

for line in lines:
    # Parse line into inputs and outputs
    input, output = line.split("|")
    input = input.lstrip().rstrip()
    output = output.lstrip().rstrip()

    # Find initial words
    in_words = [set(word) for word in input.split(" ")]
    for word in in_words:
        if len(word)==2:
            one = word
        elif len(word)==4:
            four = word
        elif len(word)==3:
            seven = word
        elif len(word)==7:
            eight = word

    # Now we will deduce each segment from their coincidences in each word
    seg_a = seven - one
    seg_a_on = [word for word in in_words if seg_a.issubset(word)]
    seg_g_on = [word for word in seg_a_on if not word==seven]
    seg_g = set.intersection(*seg_g_on)
    five_segs = [word for word in in_words if len(word)==5]
    seg_d = set.intersection(*five_segs) - (set.union(seg_a,seg_g))
    seg_b = four - set.union(seven,seg_d)
    five = [word for word in five_segs if seg_b.issubset(word)][0]
    seg_f = set.intersection(one,five)
    seg_c = one - seg_f
    seg_e = eight - set.union(seg_a,seg_b,seg_c,seg_d,seg_f,seg_g)

    # With segments deduced, construct our remaining display characters
    zero = eight - seg_d
    two = eight - set.union(seg_b,seg_f)
    three = eight - set.union(seg_b,seg_e)
    six = eight - seg_c
    nine = eight - seg_e

    # Now parse our outputs
    out_words = [set(word) for word in output.split(" ")]
    line_answer = ""
    for word in out_words:
        if word == zero:
            line_answer += "0"
        elif word == one:
            line_answer += "1"
            part_one_answer += 1
        elif word == two:
            line_answer += "2"
        elif word == three:
            line_answer += "3"
        elif word == four:
            line_answer += "4"
            part_one_answer += 1
        elif word == five:
            line_answer += "5"
        elif word == six:
            line_answer += "6"
        elif word == seven:
            line_answer += "7"
            part_one_answer += 1
        elif word == eight:
            line_answer += "8"
            part_one_answer += 1
        elif word == nine:
            line_answer += "9"
    #print(output+": {}".format(line_answer))
    part_two_answer += int(line_answer)

print("\n")
print("Part One Answer: {}".format(part_one_answer))
print("Part Two Answer: {}".format(part_two_answer))
print("\n")
