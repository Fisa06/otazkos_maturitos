# Ukázka pro všechny části otázky o cyklech

import random

print("1. while cyklus (zadání hesla):")
heslo = ""
while heslo != "tajne":
    heslo = "tajne"  # Simulace vstupu pro potřeby ukázky
    print(f"Zadal jsi: {heslo}")
print("Přístup povolen.\n")

print("2. Nekonečný cyklus s podmíněným přerušením:")
pocitadlo = 0
while True:
    print(f"Pokus {pocitadlo}")
    pocitadlo += 1
    if pocitadlo >= 3:
        break
print("Konec nekonečného cyklu.\n")

print("3. for cyklus s řetězcem:")
for znak in "Python":
    print(f"Písmeno: {znak}")
print()

print("4. for cyklus s range(1, 6):")
for i in range(1, 6):
    print(f"Číslo: {i}")
print()

print("5. for cyklus s continue (přeskočí 2):")
for i in range(5):
    if i == 2:
        continue
    print(f"Hodnota: {i}")
print()

print("6. Generování náhodných čísel:")
for _ in range(3):
    cislo = random.randint(1, 6)
    print(f"Náhodné číslo: {cislo}")