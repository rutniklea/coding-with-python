i = 0
vsota = 0

while True:
    stevila = float(input("Vnesi število: "))
    if stevila == 0:  #če je število enako 0
        break;  # potem končaj
    vsota += stevila
    i += 1

print("Vsota vnesenih številk je: ", vsota)
