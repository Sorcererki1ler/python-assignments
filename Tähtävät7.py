pituus = int(input("Anna kuhan pituus (cm): "))
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen, se on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on sallitun mittainen, voit pitää sen.")