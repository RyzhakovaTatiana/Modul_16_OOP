#Напишите код для описания геометрической фигуры.
#Создайте класс «прямоугольник» с помощью метода  __init__().
# На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями.

class rectangle:
    def __init__(self, l, w ):
        self.length = l
        self.width = w

    def rec_area(self):
        return self.length*self.width

new_rectangle = rectangle(12, 10)
print(new_rectangle.length)
print(new_rectangle.width)
print(new_rectangle.rec_area())
