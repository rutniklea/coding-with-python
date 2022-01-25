i = 0
vsota = 0

while True:
    stevila = float(input("Vnesi število: "))
    if stevila == 0:
        break;
    vsota += stevila
    i += 1

print("Povrečje vnesenih številk je: ", vsota / i)