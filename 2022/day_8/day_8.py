file = open("2022\day_8\input_day_8.txt", 'r')

list_of_inputs = []

for line in file:
    line = line.strip()
    list_of_inputs.append(line)
    
visible_trees = 0
for i in range(len(list_of_inputs)):
    for j in range(len(list_of_inputs[i])):
        if i == 0 or i == len(list_of_inputs)-1 or j == 0 or j == len(list_of_inputs[i])-1:
            visible_trees += 1
        else:
            flag_is_visible = False
            value = list_of_inputs[i][j]
            tmp = [] 

            for c in range(len(list_of_inputs)):
                tmp.append(list_of_inputs[c][j])

            if max(tmp[0:i]) < value: flag_is_visible = True
            if max(tmp[i+1:len(tmp)]) < value: flag_is_visible = True
            if max(list_of_inputs[i][0:j]) < value: flag_is_visible = True
            if max(list_of_inputs[i][j+1:len(list_of_inputs[i])]) < value: flag_is_visible = True
            
            if flag_is_visible:
                visible_trees += 1

print(visible_trees)
