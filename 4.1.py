# 1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

# 2
while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        break
    print(tuumat * 2.54)

# 3
luvut = []
while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == "":
        break
    luvut.append(int(luku))
print("Pienin:", min(luvut))
print("Suurin:", max(luvut))

# 4
import random
luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break

# 5
yritykset = 0
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        yritykset += 1

# 6
import random
n = int(input("Anna arvottavien pisteiden määrä: "))
osumat = 0
i = 0
while i < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        osumat += 1
    i += 1
print("Piin likiarvo:", 4 * osumat / n)
