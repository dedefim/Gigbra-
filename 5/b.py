#Создать программу, которая считает сумму арифметической прогрессии 3, 7, 11…43.

a = 0
for i in range(3, 43, 4):
    a += i
print("Сумма членов арифметической прогресии", a)
