from turtle import *
import time


def risanje_lika(koti, stranica):
    kot = 180 - (((koti-2)*180) /koti)

    for i in range(koti):
        forward(stranica)
        left(kot)


koti = int(input("Vnesi število kotov: "))
stranica = int(input("Vnesi dolžino stranice: "))
st_likov = int(input("Vnesi število likov: "))

speed(0)

for i in range(st_likov):
    risanje_lika(koti, stranica)
    left(360/st_likov)
