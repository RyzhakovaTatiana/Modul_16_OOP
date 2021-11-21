
#Создать калькулятор

def calc(a, b, operation):
    result = "Операция не поддерживается"
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            result = "Делить на 0 нельзя"
    return result

if __name__ == "__main__":
# Чтобы предотвратить запуск кода при импорте модуля нужно писать такую конструкцию
    print(calc(30, 15, "+"))
    print(calc(30, 15, "-"))
    print(calc(20, 5, "*"))
    print(calc(25, 4, "/"))




