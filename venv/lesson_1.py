name = input("Введите имя:")
my_age = input("Введите возраст:")
print("Имя:", name, "Возраст:", my_age)


s = int(input())
h = s // 3600
h = h % 24
m = s // 60
m = m % 60
s = s % 60
print(f"{h}:{m}:{s}")


n = int(input("Число: "))
a = int(str(n) + str(n))
b = int(str(n) + str(n) + str(n))
c = n + a + b
print(f"{n} + {a} + {b} = {c}")


n = int(input("Введите целое положительное число: "))
max = n % 10
while n >=1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе:", max)
        break


d = int(input("Выручка:"))
c = int(input("Издержки:"))
if d>c:
    print("Прибыль")
else:
    print("Убыток")
if d>c:
    a = d - c
    print(a)
g = int(input("Численность сотрудников:"))
print(a // g)


a = int(input())
b = int(input())
i = 1
while a < b:
    a = a * 110 / 100
    i += 1
print(i)

