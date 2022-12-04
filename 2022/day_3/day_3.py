file = open("2022\day_3\input_day_3.txt", 'r')

counter = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp = 0
list_of_lines = list()
list_of_lines.append([])
index = 0
for line in file:
    line = line.strip()
    if tmp < 3:
        list_of_lines[index].append(line)
        tmp+=1
    elif tmp == 3:
        list_of_lines.append([])
        tmp = 1
        index += 1
        list_of_lines[index].append(line)
    
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
    for character in first_half:
        if character in second_half:
            counter += (alphabet.index(character)+1)
            break

print(counter)

counter = 0

for lines in list_of_lines:
    for character in lines[0]:
        if character in lines[1] and character in lines[2]:
            counter += (alphabet.index(character)+1)
            break

print(counter)
