from turtle import *


n = int(input("Vnesi število kotov: "))
y = int(input("Vnesi dolžino stranice: "))

kot = 100 - (((n - 2) * 180) / n)

for i in range(n):
    forward(y)
    speed(6)
    left(kot)
