stranica = int(input("vnesi število, ki bo predstavljajo dolžino stranice kvadrata: \n"))
a=0
print("Kvadrat zvezdic\n")

while(a< stranica):
    b=0
    while(b < stranica):
        b+=1
        print("*", end=" ")
    a+=1
    print()