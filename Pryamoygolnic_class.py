class Rectangle:#Это класс, который мы описываем, чтобы дальше реализовать наследование
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHight(self):
        return self.height

#Теперь описываем метод подсчета площади

    def getArea(self):
        return self.width * self.height

#Чтобы посчитать площадь прямоугольника, мы должны импортировать этот класс в наследуемый объект

#Теперь добавим квадрат

class Square:
    def __init__(self, width):
        self.width = width

    def get_area_square(self):
        return self.width ** 2

class Circle:


    def __init__(self, radius):
        self.radius = radius


    def get_area_circle(self):
        return 3.14 * self.radius ** 2

