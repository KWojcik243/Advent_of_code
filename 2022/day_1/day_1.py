import heapq


file = open("2022\day_1\input_day_1.txt", 'r')

#First part

list_elves_calories = []
list_elves_calories.append(0)
counter = 0

for line in file:
    if line == "\n":
        counter+=1
        list_elves_calories.append(0)
    else:
        list_elves_calories[counter] += int(line.strip())

print(max(list_elves_calories))

#Second part

print(sum(heapq.nlargest(3,list_elves_calories)))