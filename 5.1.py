import random

# Kysytään arpakuutioiden määrä
n = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for i in range(n):
    heitto = random.randint(1, 6)  # yksi arpakuution heitto
    summa += heitto

print(f"Silmälukujen summa on {summa}")