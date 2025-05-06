# Ukázky pro téma n-tice, slovníky a soubory

# 1. N-tice
ntice1 = (1, 2, 2)
ntice2 = (2, 3)
kombinace = ntice1 + ntice2
jednoprvkova = (100,)

# 2. Slovníky
slovnik = {"jmeno": "Petr", "vek": 30}
slovnik["mesto"] = "Praha"
del slovnik["vek"]

# Průchod slovníkem
vystup_slovnik = []
for klic in slovnik:
    vystup_slovnik.append(f"{klic} -> {slovnik[klic]}")

# 3-5. Práce se soubory (zápis, čtení, seek, tell)
cesta = "test.txt"

# Zápis do souboru
with open(cesta, "w") as f:
    f.write("Prvni radek\n")
    f.write("Druhy radek\n")

# Čtení a manipulace se souborem
with open(cesta, "r+") as f:
    vse = f.read()
    pozice_pred = f.tell()
    f.seek(0)
    prvni_radek = f.readline()
    pozice_po = f.tell()