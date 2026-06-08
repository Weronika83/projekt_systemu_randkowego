from tkinter import *
from controller import wybierz_klientow, wybierz_pracownikow, pokaz_szczegoly, dodaj_randke, pokaz_randki

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

# SZCZEGÓŁY

Label(root, text="Szczegóły").pack()

Label(root, text="Imię:").pack()
label_imie_wartosc = Label(root, text="-")
label_imie_wartosc.pack()

Label(root, text="Wiek:").pack()
label_wiek_wartosc = Label(root, text="-")
label_wiek_wartosc.pack()

Label(root, text="Opis:").pack()
label_opis_wartosc = Label(root, text="-")
label_opis_wartosc.pack()

Label(root, text="Lokalizacja:").pack()
label_lokalizacja_wartosc = Label(root, text="-")
label_lokalizacja_wartosc.pack()

Button(root, text="Pokaż szczegóły", command=pokaz_szczegoly).pack()


# RANDKI

Label(root, text="Lista randek").pack()

listbox_randki = Listbox(root, width=40, height=5)
listbox_randki.pack()

Label(root, text="Klient").pack()
entry_klient_randka = Entry(root)
entry_klient_randka.pack()

Label(root, text="Partner").pack()
entry_osoba_randka = Entry(root)
entry_osoba_randka.pack()

Label(root, text="Data").pack()
entry_data_randka = Entry(root)
entry_data_randka.pack()

Button(root, text="Dodaj randkę", command=dodaj_randke).pack()

root.mainloop()
