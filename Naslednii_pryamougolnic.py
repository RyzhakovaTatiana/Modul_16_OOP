from Pryamoygolnic_class import Rectangle

rec1 = Rectangle(10, 5)

print("rec1.width =", rec1.width)

print("rec1.height =", rec1.height)

print("rec1.getArea = ", rec1.getArea())



print("---------------------")

from Pryamoygolnic_class import Square

my_square = Square(3)

print("my_square.width = ", my_square.width)
print("my_square.getArea = ", my_square.get_area_square())

print("---------------------")


from Pryamoygolnic_class import Circle

my_circle = Circle(2)

print("my_circle_radius = ", my_circle.radius)
print("my_circle_area = ", my_circle.get_area_circle())

print("---------------------")

figures = [rec1, my_square, my_circle]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.getArea())