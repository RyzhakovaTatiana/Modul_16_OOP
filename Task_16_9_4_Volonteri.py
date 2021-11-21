#Команда проекта планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.

# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
#При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"


class Corporativ:
    def __init__(self, person_name="", person_lastname="", city="", status=""):
        self.person_name = person_name
        self.person_lastname = person_lastname
        self.city = city
        self.status = status

    def go_to_corporative(self, volonter):
        self.person_name = volonter.get("person_name")
        self.person_lastname = volonter.get("person_lastname")
        self.city = volonter.get("city")
        self.status = volonter.get("status")

    def get_name(self):
        return self.person_name

    def get_lastname(self):
        return self.person_lastname


    def get_city(self):
        return self.city

    def get_status(self):
        return self.status

IvanPetrov = Corporativ(person_name="Иван", person_lastname="Петров", city="г. Москва", status="Наставник")

print(IvanPetrov.get_name(), IvanPetrov.get_lastname(), ",", IvanPetrov.get_city(), ", статус: ", IvanPetrov.get_status())












