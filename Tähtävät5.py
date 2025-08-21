leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

total_grams = (leiviska * 20 * 32 * 13.3) + (naula * 32 * 13.3) + (luoti * 13.3)

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"Massa nykymittojen mukaan: {kilograms} kilogrammaa ja {grams:.2f} grammaa")
