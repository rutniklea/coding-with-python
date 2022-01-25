import random

kamen = 1
papir = 2
skarje = 3

racunalnik_score = 0
uporabnik_score = 0

while True:
    racunalnik = random.randint(1, 3)
    uporabnik = int(input(" Vnesi število (1-KAMEN, 2-PAPIR, 3-ŠKARJE): "))
    if racunalnik == kamen and uporabnik == papir:
        uporabnik_score += 1
    elif racunalnik == papir and uporabnik == skarje:
        uporabnik_score += 1
    elif racunalnik == skarje and uporabnik == kamen:
        uporabnik_score += 1
    elif uporabnik == kamen and racunalnik == papir:
        racunalnik_score += 1
    elif uporabnik == papir and racunalnik == skarje:
        racunalnik_score += 1
    elif uporabnik == skarje and racunalnik == kamen:
        racunalnik_score += 1
    print(f"Uporabnik ima: {uporabnik_score} točk, računalnik ima: {racunalnik_score} točk. ")

    if racunalnik_score == 5 or uporabnik_score == 5:
        break
