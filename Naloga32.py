pozitivna_st = 0
negativna_st = 0
vsota =0

while True:
    i = int(input("Prosim vnesi številko: "))
    if (i == 0):
        break
        if(i > 0):
            vsota +=1
            pozitivna_st += 1
        elif (i < 0):
            negativna_st -= 1


print("\nSkupno število pozitivnih števil =  ", pozitivna_st)
print("Skupno število negativnih števil =  ", negativna_st)


