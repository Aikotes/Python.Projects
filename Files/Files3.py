file = open(r"G:\HDD\Data\Python.Projects\Files\MyFile.txt","r")
line = " "
run = 1
while run == 1:
    line = file.read(5)
    position = int(file.tell())
    if line == "":
        run = 0
    if line != "":       
        if line != "World":
             result = "fail"
             file.seek(position-4)
    if line == "World":
        run = 0
        result = "sucess"
file.seek(position-1)
print(result,"Position=",position,"CurrentSymbol=",file.read(1))
file.close()
