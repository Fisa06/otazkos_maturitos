import math
import random

# 2. Definice a volání funkce
def soucet(a, b):
    return a + b

# 3. Typy parametrů
def mocnina(x, y=2):
    return x ** y

def vypis(*data):
    for prvek in data:
        print("Prvek:", prvek)

# 4. Návratová hodnota
def vypocet():
    return 5 * 2

# 5. Lokální a globální proměnné
x = 10
def zmenit():
    global x
    x = 20

# 7. Lambda funkce
nasobeni = lambda a, b: a * b

# 8. Použití modulu
odmocnina = math.sqrt(25)
nahodne_cislo = random.randint(1, 100)

# Výstupy
print("2) soucet(3, 4):", soucet(3, 4))
print("3) mocnina(3):", mocnina(3))
print("3) mocnina(3, 3):", mocnina(3, 3))
print("3) vypis('a', 'b', 'c'):")
vypis("a", "b", "c")
print("4) vypocet():", vypocet())
print("5) Globální před změnou:", x)
zmenit()
print("5) Globální po změně:", x)
print("7) nasobeni(5, 6):", nasobeni(5, 6))
print("8) math.sqrt(25):", odmocnina)
print("8) random.randint(1, 100):", nahodne_cislo)