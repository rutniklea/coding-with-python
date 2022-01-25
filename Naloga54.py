
beseda= input("vnesi skrito besedo: ")
prazno = []
poskuz=13

for i in beseda:
    prazno.append("_")

for i in range(len(beseda)*3):
    crka = input(f"vnesi črko: , ({poskuz}, poskusov.): ")
    poskuz -= 1
    for a in range(len(beseda)):
        if crka == beseda[a]:
            prazno[a] = crka
    print("".join(prazno))

    if "_" not in prazno:
        print("Bravo, pravilno si ugotovil/a pravo besedo! ")
        break




