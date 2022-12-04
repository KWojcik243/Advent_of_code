import re

file = open("2022\day_4\input_day_4.txt", 'r')

#First part

counter = 0 
second_part_counter = 0

for line in file:
    line = line.strip()
    line = re.split("-|,| ",line)
    if int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3]):
        counter += 1
        second_part_counter += 1
    elif int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3]):
        counter += 1
        second_part_counter += 1
        #Second part
    elif int(line[0]) <= int(line[3]) and int(line[2]) <= int(line[1]):
        second_part_counter += 1


print(counter)
print(second_part_counter)
