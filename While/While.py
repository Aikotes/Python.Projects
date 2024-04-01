import os
run = 1
os.system('cls')
while run == 1:
 result = 0
 os.system('cls')
 print("MENU")
 print("")
 print("1,Сложить")
 print("2.Умножить")
 print("3.Вычесть")
 print("4.Делить")
 print("5.Выход")
 chose = int(input())
 os.system('cls')
 if chose != 5:
     print("Введите 1 число")
     chislo1 = int(input())
     os.system('cls')
     print("Введите 2 число")
     chislo2 = int(input())
     os.system('cls')
 if chose == 1:
     result = (chislo1+chislo2)
 if chose == 2:
     result = (chislo1*chislo2)
 if chose == 3:
     result = (chislo1-chislo2)
 if chose == 4:
     result = (chislo1/chislo2)
 if chose == 5:
     run = 0 
 if chose != 5:     
     print("Ответ:",result)
     print("Продолжить? y/n")
     chose = str(input())
     if chose == "n":
         run = 0
 
 