def narisi_polje(polje):
    for y in range(len(polje)):
        for x in range(len(polje[y])):
            print(polje[y][x], end=" ")
        print()

def ustvari_polje(sirina, visina):
    polje = []
    for y in range(visina):
        vrsta = []
        for y in range(sirina):
            vrsta.append(".")
        polje.append(vrsta)
    return polje

def visina_zetona(polje, x):
    for y in range(len(polje)):
        if "." != polje[y][x]:
            return y-1
    return len(polje) -1

polje = ustvari_polje(7,7)

narisi_polje(polje)

while True:
    x = int(input("Vnesi x: " ))
    y= visina_zetona(polje,x)

    polje[y][x] = "x"
    narisi_polje(polje)

    x = int(input("Vnesi O: "))
    y = visina_zetona(polje, x)
    polje[y][x] = "O"
    narisi_polje(polje)


