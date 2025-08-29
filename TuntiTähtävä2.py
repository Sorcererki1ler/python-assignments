physics = float(input("Anna fysiikan tulos: "))
math = float(input("Anna matematiikan tulos: "))
chem = float(input("Anna kemian tulos: "))

if physics < 50 or math < 50 or chem < 50:
    print("Et saa stipendiä, koska jokin tulos on alle 50.")
elif (physics > 90 and math > 90) or chem > 95:
    print("Saat stipendin!")
else:
    print("Et saa stipendiä.")
