# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# m = a
#
# if m < b:
#     m = b
# if m < c:
#     m = c
#
# print("Наибольшее значение будет равно: ", m)


#Игра Угадай число
import random
num = random.randint(1, 100)
while True:
    print("Угадайте число от 1 до 100")
    guess = int(input("Введите число: "))
    if guess == num:
        print("Вы угадали!")
        break
    elif guess < num:
        print("Загаданное число больше")
        print("-------------------")
    elif guess > num:
        print("Загаданное число меньше")
        print("-------------------")


