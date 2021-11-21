#Вычислить факториал через цикл

#n = int(input("Введите число "))
#factorial1 = 1
#while n > 1:
    #factorial1 *= n
    #n = n - 1
#print(factorial1)

print("------------------")
n2 = int(input("Введите число "))
factorial2 = 1

for i in range(2, n2 + 1):
    factorial2 *= i
print(factorial2)


print("------------------")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")