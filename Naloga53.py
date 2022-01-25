#Uporabnik vnese besedilo. Zamenjaj tretjo besedo.


besedilo = input("Vnesite besedilo: ")

novo = besedilo.split()
novo[2] = "čuden" #2 ker je prva besedla na 0 točki

print(novo)

besedilo2= " ".join(novo)
print(besedilo2)