import os
def Write(adress,position,char):
    if os.path.exists(adress):
        file = open(adress,"r+")
        if position != 0:
            position = (position-1)
        file.seek(position)
        file.write(char)
        file.close()
    else:
        file = open(adress,"w")
        if position != 0:
            position = (position-1)
        file.seek(position)
        file.write(char)
        file.close()
def Read(adress,position,lenght):
    file = open(adress,"r")
    file.seek(position-1)
    return(file.read(lenght))
    file.close()
def Search(adress,string,length):
    file = open(adress)
    run = 1
    position = file.tell()
    while run == 1:
        line = file.read(lenght)
        if line != "":
            if line == string:
                return(position)
                run = 0
            if line != string:
                position = (position+1)
                position = (position-lenght)
                file.seek(position)
        if line == "":
            run = 0
def Clear(adress):
    if os.path.exists(adress):
        file = open(adress,"w")
        file.close()
    else:
        print("Файл не существует")