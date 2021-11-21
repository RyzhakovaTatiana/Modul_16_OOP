#Нужно посчитать количество четных и нечетных цифр во введенном числе

import math

a = int(input("Введите число: "))
even = 0#четные
odd = 0#нечетные

while a > 0:
    if a % 2 ==0:
        even += 1
    else:
        odd += 1
    a = a // 10
print("Even: %d, odd: %d" % (even, odd))

