class File:
    def __init__(self, name, size) -> None:
        self.name=name
        self.size=size


class Directory:
    def __init__(self, name) -> None:
        self.size = 0
        self.children_list = []
        self.files = []
        self.name = name
        self.parent = ""

    def addDict(self, child):
        self.children_list.append(child)
    
    def addFile(self, file):
        self.files.append(file)
        self.changeSize(file.size)
    
    def changeSize(self, size):
        self.size += int(size)
        if self.parent != "":
            self.parent.changeSize(size)

file = open("2022\day_7\input_day_7.txt", 'r')

main_dir = Directory("/")
actual_dir = main_dir

for line in file:
    line = line.strip()
    if line.startswith("$ cd"):
        line = line.split(" ")
        if line[2] =="/":
            actual_dir=main_dir
        elif line[2] =="..":
            try:
                actual_dir = actual_dir.parent
            except:
                pass
        else:
            for dir_child in actual_dir.children_list:
                if dir_child.name == line[2]:
                    actual_dir = dir_child
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("dir"):
        directory = Directory(line.split(" ")[1])
        directory.parent = actual_dir
        actual_dir.addDict(directory)
    else:
        line = line.split(" ")
        object_file = File(line[1], line[0])
        actual_dir.addFile(object_file)

size_counter = 0

def dfs(directory):
    global size_counter
    for child in directory.children_list:
        print(child.name)
        if(child.size < 100000):
            size_counter += child.size
        dfs(child)

print(dfs(main_dir))
