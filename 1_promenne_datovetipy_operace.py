# 1. Proměnné
jmeno = "Anna"
vek = 18

# 2. Operátory přiřazení
a = 6
print("a =>", a)
a += 6
print("a += 6 =>", a)
a -= 2
print("a -= 2 =>", a)
a *= 2
print("a *= 2 =>", a)
a /= 4
print("a /= 4 =>", a)

# 3. Datové typy
cislo = 42            # int
cena = 3.14           # float
text = "ahoj"         # str
pravda = True         # bool
seznam = [1, 2, 3]    # list
slovnik = {"jmeno": "Eva", "vek": 20}  # dict
mnozina = {1, 2, 3}   # set
troice = (1, 2, 3)    # tuple

# 4. Převodní funkce
print(int("5"))       # 5
print(str(10))        # "10"
print(float("2.7"))   # 2.7
print(bool(0))        # False
print(chr(65))        # "A"
print(ord("A"))       # 65

# 5. Vstup a výstup
# jmeno = input("Zadej jméno: ")
# print("Ahoj,", jmeno)

# 6. Aritmetické operace
print(3 + 2)      # 5
print(5 - 3)      # 2
print(4 * 2)      # 8
print(5 / 2)      # 2.5
print(5 // 2)     # 2
print(5 % 2)      # 1
print(2 ** 3)     # 8

# 7. Import a knihovny
import math
print(math.sqrt(16))      # 4.0

# 8. Knihovna math
print(math.floor(3.9))           # 3
print(math.ceil(3.1))            # 4
print(math.sin(math.radians(30))) # 0.5
print(math.radians(90))          # 1.570...

# 9. Komentáře
# Toto je jednořádkový komentář
"""
Toto je víceřádkový komentář
Používá se například pro dokumentaci
"""
