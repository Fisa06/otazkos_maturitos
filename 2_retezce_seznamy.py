# Ukázky pro otázku 2: Řetězce a seznamy

# 1. Řetězce a indexování
text = "ahoj"
print(text[0])     # a
print(text[-1])    # j
print("Ahoj" + " Světe")
print("-" * 5)

# 2. Operace s řetězci
print("a" == "a")
print("b" > "a")
print("a" in "auto")

# 3. Escape znaky
print("Ahoj\nsvěte")
print("\tTabulátor")
print("\"Text v uvozovkách\"")

# 4. f-string
jmeno = "Eva"
print(f"Ahoj, {jmeno}!")
x = 5
print(f"Dvojnásobek: {x * 2}")

# 5. Slice
text = "programovani"
print(text[2:5]) # "ogr"
print(text[:5])  # "progr"
print(text[5:])  # "amovani"
print(text[::2]) # "pormoani"

# 6. Seznamy a indexování
cisla = [1, 2, 3, 4]
print(cisla[0])   # 1
print(cisla[-1])  # 4

# 7. Operace se seznamy
cisla[1] = 10
print(cisla + [5, 6])
print(cisla * 2)
print([1, 2] == [1, 2])
print([1, 2] is [1, 2])

# 8. Metody seznamů
seznam = [1, 2, 2, 3]
print(seznam)
seznam.append(4)
print(seznam)
seznam.insert(1, 10)
print(seznam)
print(seznam.count(2))
seznam[0] = 99
print(seznam)
print("Odstraněný prvek:", seznam.pop())
print("Zbývající seznam:", seznam)
print("Poslední prvek:", seznam[-1])

# 9. Datum a čas
from datetime import datetime
import time

cas = datetime.now()
print("Aktuální čas:", cas)
print("Hodina:", cas.hour, "Minuta:", cas.minute)

print("Čas v sekundách:", time.time())
time.sleep(1)
print("Pauza 1 sekunda dokončena")


