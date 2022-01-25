vrsta = int(input("Vnesi število vrstic: \n"))

for a in range(vrsta):
    for b in range(a+1): # se poveča za eno
        print("*", end=" ")
    print("\n")