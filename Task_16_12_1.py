import math
# print ("Введите длины сторон треугольника")
#
# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))
#
# p = a + b + c / 2
#
# s = math.sqrt(p * (p-a) * (p-b) * (p - c))
#
# print("P=%d; S=%.2f" % (a + b + c, s))
#
# print ("Введите радиус круга")
#
# r = int(input("r= "))
# print("P=%.2f; S=%.2f" % (2 * math.pi * r, math.pi * r ** 2))



print("1 - прямоугольник, 2- треугольник, 3 - круг")

figure = input("Выберите фигуру: ")

if figure == "1":
    a = float(input("а = "))
    b = float(input("b = "))
    print("Площадь прямоугольника: %.2f" % (a * b))

elif figure == "2":
    a = float(input("а = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Периметр треугольника: %.2f; Площадь треугольника: %.2f" % (p, s))

elif figure == "3":
    r = float(input("Радиус круга r = "))
    print("Площадь круга = %.2f" % (math.pi * r ** 2))

else:
    print("Ошибка ввода")