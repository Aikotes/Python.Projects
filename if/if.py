print ("MENU")
print("")
print("Что делаем?")
print("1.Сложение")
print("2.Вычитание")
print("3.Деление")
print("4.Умножение")
dei = int(input())
print ("Введите 1 число")
chislo1 = int(input())
print("Введите 2 число")
chislo2 = int(input())
if dei == 1:
    result = (chislo1+chislo2)
if dei == 2:
    result = (chislo1-chislo2)
if dei == 3:
    result = (chislo1/chislo2)
if dei == 4:
    result = (chislo1*chislo2)
print("Ответ:",result)