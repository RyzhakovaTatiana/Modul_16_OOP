import math
#Перевернуть число. Вводится целое число.
#Нужно вывести число в обратном порядке составляющих его чисел
#На вход подается число 3425, на выводе 5243

num = int(input("Введите целое число: "))



num1 = 0#Тут храним изначальный 0, чтобы потом сюда записать значение

while num > 0:
    digit = num % 10#последняя цифра
    num = num // 10#удаляем последнюю цифру
    num1 = num1 * 10
    num1 = num1 + digit
print("Обратное ему число: ", num1)

