file = open(r"G:\HDD\Data\Python.Projects\Files\MyFile.txt","r+")
run = 1
result = "fail"
while run == 1:
    line = file.read(2)
    position = file.tell()
    if line != "":
        if line == "o ":
            file.seek(position-2)
            line.strip()
            file.write(line)
            run = 0;
            result = "sucess"
        if line !="o ":
            position = (position-1)
            file.seek(position)
    if line == "":
        run = 0    
print("Result=",result)
file.close()