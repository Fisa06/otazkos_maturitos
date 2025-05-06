import numpy as np
import matplotlib.pyplot as plt

# 1. Výpočet funkce
print("sin(pi/2):", np.sin(np.pi / 2))

# 2. Vytvoření vektorů
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.arange(0, 5, 0.5)

# 3. Základní graf s legendou
plt.figure()
plt.plot(x, y, label="sin(x)", color="blue")
plt.legend(loc="upper right")
plt.title("Sinusová křivka")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# 4. Subploty
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), label="sin")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), label="cos", color="red")
plt.legend()

# 5. Plocha mezi křivkami
plt.figure()
y1 = np.sin(x)
y2 = 0.5 * np.sin(x)
plt.fill_between(x, y1, y2, where=(y1 > y2), facecolor="lightgreen")
plt.plot(x, y1, label="y1")
plt.plot(x, y2, label="y2")
plt.legend()

# 6. Text a anotace
plt.text(2, 0.5, "Maximální rozdíl")
plt.annotate("Vrchol",
             xy=(np.pi/2, 1),
             xytext=(2, 1.2),
             arrowprops=dict(arrowstyle="->", color="black"))

plt.show()
