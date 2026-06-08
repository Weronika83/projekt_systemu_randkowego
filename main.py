from tkinter import *
from controller import wybierz_klientow, wybierz_pracownikow

root = Tk()
root.title("Portal randkowy")
root.geometry("1100x760")

Label(root, text="Wybierz moduł").pack()

Button(root, text="Klienci", command=wybierz_klientow).pack()
Button(root, text="Pracownicy", command=wybierz_pracownikow).pack()

# FORMULARZ

Label(root, text="Imię").pack()
entry_imie = Entry(root)
entry_imie.pack()

Label(root, text="Wiek").pack()
entry_wiek = Entry(root)
entry_wiek.pack()

Label(root, text="Opis zainteresowań").pack()
entry_opis = Entry(root)
entry_opis.pack()

Label(root, text="Lokalizacja").pack()
entry_lokalizacja = Entry(root)
entry_lokalizacja.pack()

# PRZYCISKI CRUD

Button(root, text="Dodaj").pack()
Button(root, text="Edytuj").pack()
Button(root, text="Usuń").pack()

root.mainloop()