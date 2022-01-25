import time
import random

start = time.time()

stevec = 0

besedilo = "Naša različica Lorem Ipsuma temelji na slovarju z več kot 200 latinskimi besedami, ki se s pomočjo modela stavčnih struktur povezujejo v bolj smiselne stavke. Generirano Lorem Ipsum besedilo je tako brez ponavljanj, šaljivih vložkov in neprimernih vrinjenih besed ter drugih neprijetnih dodatkov."

besede = besedilo.split()

while True:
    beseda = besede[random.randint(0, len(besede))]
    up_beseda = input(f"Vnesi besedilo:[ {beseda} ]: ")
    if up_beseda == beseda:
        stevec += 1
    if stevec == 10:
        break


end = time.time()
dd = end - start
print(f"Porabili ste {dd}/sekund za izpis vseh besed. ")
