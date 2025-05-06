import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor

# Funkce pro událost kliknutí
def klikni(event):
    print("Kliknuto na:", event.x, event.y)

# Otevření souboru
def otevri():
    soubor = filedialog.askopenfilename()
    if soubor:
        messagebox.showinfo("Soubor", f"Vybral jsi: {soubor}")

# Výběr barvy
def vyber_barvu():
    barva = askcolor()[1]
    print("Zvolená barva:", barva)

# Hlavní okno
root = tk.Tk()
root.title("GUI II")
root.geometry("400x400")

# Spinbox
cislo = tk.IntVar()
sp = tk.Spinbox(root, from_=0, to=10, textvariable=cislo)
sp.pack()

# Text
text = tk.Text(root, height=4)
text.insert("1.0", "Víceřádkové pole")
text.pack()

# Canvas
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()
canvas.create_oval(50, 50, 150, 150, fill="blue")
canvas.bind("<Button-1>", klikni)

# Menu
menu = tk.Menu(root)
soubor_menu = tk.Menu(menu, tearoff=0)
soubor_menu.add_command(label="Otevřít", command=otevri)
menu.add_cascade(label="Soubor", menu=soubor_menu)

barva_menu = tk.Menu(menu, tearoff=0)
barva_menu.add_command(label="Změnit barvu", command=vyber_barvu)
menu.add_cascade(label="Barva", menu=barva_menu)

root.config(menu=menu)

root.mainloop()
