from copy import deepcopy


file = open("2022\day_5\input_day_5.txt", 'r')

list_of_stacks = []
list_of_stacks.append("WBGZRDCV"[::-1])
list_of_stacks.append("VTSBCFWG"[::-1])
list_of_stacks.append("WNSBC"[::-1])
list_of_stacks.append("PCVJNMGQ"[::-1])
list_of_stacks.append("BHDFLST"[::-1])
list_of_stacks.append("NMWTVJ"[::-1])
list_of_stacks.append("GTSCLFP"[::-1])
list_of_stacks.append("ZDB"[::-1])
list_of_stacks.append("WZNM"[::-1])
list_of_stacks_part2 = deepcopy(list_of_stacks)

for line in file:
    line = line.strip()

    if line.startswith("move"):
        line = line.strip()
        line = line.split(" ")
        for i in range(int(line[1])):
            character = list_of_stacks[int(line[3])-1][-1]
            list_of_stacks[int(line[3])-1] = list_of_stacks[int(line[3])-1][:-1]
            list_of_stacks[int(line[5])-1] += character

        substr_to_move = list_of_stacks_part2[int(line[3])-1][-int(line[1]):]
        list_of_stacks_part2[int(line[3])-1] = list_of_stacks_part2[int(line[3])-1][:-int(line[1])]
        list_of_stacks_part2[int(line[5])-1] += substr_to_move

result_part_1 = ""
result_part_2 = ""
for line, line_part_2 in zip(list_of_stacks, list_of_stacks_part2):
    result_part_1 += line[-1]
    result_part_2 += line_part_2[-1]

print(result_part_1)
print(result_part_2)
