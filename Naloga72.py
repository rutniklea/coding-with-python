import time
from turtle import *

def odstevalnik():
    for i in range(5,0,-1):
        clear()
        time.sleep(0.2)
        write(i, font=['Raleway', 22, "normal"])
        time.sleep(1)
    clear() # pobrišemo, ko se zanka konča

def klik_miske(x,y):
    global st_klikov, start  #globalna spremenljivka
    trenutni_cas = time.time()
    cas = trenutni_cas - start
    if cas < 5:
        clear()
        st_klikov +=1
        write(f"število klikov: {st_klikov}", align="center", font=['Raleway', 22, "underline"])
    else:
        clear()
        write(f"Uporabnik je naredil {st_klikov} klikov v 5 sekundah", align="center", font=['Raleway', 22, "underline"])
        time.sleep(10)
        exit()

odstevalnik()

st_klikov = 0
start = time.time()

screen = Screen() # naredi elemente
screen.onclick(klik_miske)
screen.listen() #posluša za evente
screen.mainloop() #vsak rabi na koncu zanko