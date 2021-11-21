#Cкоро появится новая услуга: электронный кошелек.
# То есть система будет хранить данные о своих клиентах и об их финансовых операциях.

#Нужно написать программу, обрабатывающую данные, и
# на выходе в консоль получить следующее: Клиент "Иван Петров". Баланс: 50 руб.



#Определим класс Клиенты
class Clients():

    def __init__(self, name, last_name, balance, valute):
        self.name = name
        self.last_name = last_name
        self.balance = balance
        self.valute = valute

    # Определим метод Узнать баланс
    def know_balance(self, client_balance):
        self.name = client_balance.get("name")
        self.last_name = client_balance.get("last_name")
        self.balance = client_balance.get("balance")
        self.valute = client_balance.valute("valute")

IvanPetrov = Clients(name = "Ivan", last_name= "Petrov", balance= 50, valute= "rub")
print("Клиент", IvanPetrov.name, IvanPetrov.last_name, "Баланс", IvanPetrov.balance, IvanPetrov.valute)

print(f"Клиент {IvanPetrov.name} {IvanPetrov.last_name}. Баланс {IvanPetrov.balance} {IvanPetrov.valute}")

