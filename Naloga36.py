skrita_st =int(input("Vnesi skrito število: "))
ugani = int(input("Vnesi številko med 0 in 99: "))

while skrita_st != "ugani":
    print()
    if ugani < skrita_st:
        print("Številka je večja od: ", ugani)
        ugani = int(input("Vnesi številko med 0 in 99: "))
    elif ugani > skrita_st:
        print("Številka je manjša od:", ugani)
        ugani = int(input("Vnesi številko med 0 in 99: "))
    else:
        print("BRAVO! Uganil/a si skrito številko!\n SKRITA ŠTEVILKA JE:", skrita_st, ".")
        break



