file = open("2022\day_8\input_day_8.txt", 'r')

list_of_inputs = []

for line in file:
    line = line.strip()
    # print(line)
    list_of_inputs.append(line)
    
visible_trees = 0

for i in range(len(list_of_inputs)):
    for j in range(len(list_of_inputs[i])):
        # print(j)
        if i == 0 or i == len(list_of_inputs)-1 or j == 0 or j == len(list_of_inputs[i])-1:
            visible_trees += 1
        else:
            print(i ,j)
            print(list_of_inputs[i][j])
            flag = False
            for h in range(0,i):
                if list_of_inputs[i][j] <= list_of_inputs[h][j]:
                    flag = True
            if flag == False:
                visible_trees += 1
                # print(i, j)
                print(list_of_inputs[i][j])
                # break
            # flag = False
            if flag == True:
                for h in range(i+1,len(list_of_inputs)):
                    # print(h)
                    if i == 97:
                        print(h)
                        print(list_of_inputs[h][j])
                    if list_of_inputs[i][j] <= list_of_inputs[h][j]:
                        flag = True
                if flag == False:
                    visible_trees += 1
                    # print(i, j)
                    print(list_of_inputs[i][j])
                # break
            # flag = False
            if flag == True:
                for h in range(0,j):
                    if list_of_inputs[i][j] <= list_of_inputs[i][h]:
                        flag = True
                if flag == False:
                    visible_trees += 1
                    # print(i, j)
                    print(list_of_inputs[i][j])
                    # break
            # flag = False
            if flag == True:
                for h in range(j+1,len(list_of_inputs[i])):
                    if list_of_inputs[i][j] <= list_of_inputs[i][h]:
                        flag = True
                if flag == False:
                    visible_trees += 1
                    # print(i, j)
                    print(list_of_inputs[i][j])
                # break
            # if list_of_inputs[i][j] > list_of_inputs[i][j-1] or \
            # list_of_inputs[i][j] > list_of_inputs[i][j+1] or \
            # list_of_inputs[i][j] > list_of_inputs[i+1][j] or \
            # list_of_inputs[i][j] > list_of_inputs[i-1][j]:
            #     visible_trees += 1
print(visible_trees)
#392 za mało
#927 za mało
