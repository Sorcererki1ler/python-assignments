consumption = float(input("Anna sähkönkulutus (kWh): "))
bill = 0

if consumption <= 50:
    bill = consumption * 0.10
elif consumption <= 200:
    bill = 50 * 0.10 + (consumption - 50) * 0.08
else:
    bill = 50 * 0.10 + 150 * 0.08 + (consumption - 200) * 0.06

print(f"Sähkölasku on {bill:.2f} euroa")