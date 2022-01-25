import random
import time
from turtle import *

besede = open("besedilo.txt", "r")  # r je mišljeno za read
besede = besede.readlines()
filter = []  # ustvarimo sprazni spisek za filter

screen = Screen()
screen.bgcolor("purple")

for i in range(len(besede)):
    if len(besede[i]) >= 5:
        filter.append(besede[i])

while True:
    i = random.randint(0, len(filter) - 1)
    beseda = filter[i]
    penup()
    goto(random.randint(-500, 500), random.randint(-500, 500))
    pendown()
    clear()
    write(beseda, font=["Arial", 22, "bold"])
    time.sleep(1)
