
file = open("2022\day_6\input_day_6.txt", 'r')

#First part

line_from_file = ""
for line in file:
    line_from_file = line

for i in range(len(line_from_file)-3):
        tmp = line_from_file[i:i+4]
        if tmp.count(tmp[0])==1 and tmp.count(tmp[1])==1 and tmp.count(tmp[2])==1 and tmp.count(tmp[3])==1:
            print(i+4)
            break

#Second part

for i in range(len(line_from_file)-13):
    flag = True
    tmp = line_from_file[i:i+14]
    for j in range(14):
        if tmp.count(tmp[j]) != 1:
            flag = False
    if flag:
        print(i+14)
        break
