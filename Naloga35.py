import math

seznam = []

for i in range(0, 1000):
    stevilka = int(input("Vnesi število: "))
    seznam.append(stevilka)
    if stevilka == 0:  # ali je število enako 0
        break;

print("Najmanjše število je: ", min(stevilka))

