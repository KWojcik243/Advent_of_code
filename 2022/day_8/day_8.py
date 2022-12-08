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

            # Part 2

            score = 0
            first,second,third,fourth = 0,0,0,0
            tmp_first_half = tmp[0:i]
            tmp_first_half = tmp_first_half[::-1]
            tmp_second_half = tmp[i+1:len(tmp)]
            print(tmp_second_half)
            for c in tmp_first_half:
                if c >= value:
                    first +=1
                    break
                else:
                    first +=1
            
            for c in tmp_second_half:
                if c >= value:
                    second +=1
                    break
                else:
                    second +=1
            horizontally_first_half = list_of_inputs[i][0:j]
            horizontally_first_half = horizontally_first_half[::-1]
            for c in horizontally_first_half:
                if c >= value:
                    third +=1
                    break
                else:
                    third +=1
            for c in list_of_inputs[i][j+1:len(list_of_inputs[i])]:
                if c >= value:
                    fourth +=1
                    break
                else:
                    fourth +=1

            if score < first*second*third*fourth:
                score = first*second*third*fourth

            







            

print(visible_trees)
print(score)
