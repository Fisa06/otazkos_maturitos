# 1. Podmíněný příkaz
x = int(input("Zadej číslo: "))
if x > 0:
    print("Kladné číslo")

# 2. Relační a logické operátory
if x != 0 and x < 10:
    print("Číslo je nenulové a menší než 10")

# 3. Úplné a vícecestné větvení
if x > 0:
    print("Kladné")
elif x < 0:
    print("Záporné")
else:
    print("Nula")

# 4. Výjimky – převod na celé číslo
try:
    y = int(input("Zadej další číslo: "))
    print("Zadal jsi:", y)
except ValueError:
    print("To není číslo!")

# 5. Výjimka s else a finally
try:
    z = 10 / int(input("Zadej dělitel: "))
except ZeroDivisionError:
    print("Nulou nelze dělit!")
else:
    print("Výsledek dělení je:", z)
finally:
    print("Operace dokončena.")
