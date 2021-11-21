n = int(input("Введите трехзначное число: "))

num1 = n % 10
print("Третье число = ", num1)

num2 = n % 100 // 10

print("Число в центре = ", num2)

num3 = n // 100

print("Первое число = ", num3)

print("Сумма цифр = ", num1 + num2 + num3)



