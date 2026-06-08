from tkinter import *
from tkinter import messagebox
from model import klient, pracownik, randka, klienci, pracownicy, randki

label_lista = None
label_opis = None
label_imie_wartosc = None
label_wiek_wartosc = None
label_opis_wartosc = None
label_lokalizacja_wartosc = None
listbox_klienci = None
listbox_randki = None
entry_imie = None
entry_wiek = None
entry_opis = None
entry_lokalizacja = None
entry_klient_randka = None
entry_osoba_randka = None
entry_data_randka = None
button_dodaj = None

aktualna_lista = klienci
aktualny_typ = "klient"
edytowany_indeks = None


#----------------WYBÓR MODUŁU----------------
def wybierz_klientow():
    global aktualna_lista, aktualny_typ, edytowany_indeks
    aktualna_lista = klienci
    aktualny_typ = "klient"
    edytowany_indeks = None
    label_lista.config(text="Lista klientów")
    label_opis.config(text="Opis zainteresowań:")

    pokaz_liste()

def wybierz_pracownikow():
    global aktualna_lista, aktualny_typ, edytowany_indeks
    aktualna_lista = pracownicy
    aktualny_typ = "pracownik"
    edytowany_indeks = None
    label_lista.config(text="Lista pracowników")
    label_opis.config(text="Stanowisko:")

    pokaz_liste()

# -------------------- LISTA --------------------
def pokaz_liste() -> None:
    listbox_klienci.delete(0, END)
    for i, obiekt in enumerate(aktualna_lista):
        if aktualny_typ == "klient": listbox_klienci.insert(i, f"{obiekt.imie} - {obiekt.wiek}")
        else:
            listbox_klienci.insert(i, f"{obiekt.imie} - {obiekt.stanowisko}")

#----------------DODAWANIE, USUWANIE, EDYTOWANIE----------------
def dodaj_obiekt():
    imie = entry_imie.get()
    wiek = entry_wiek.get()
    opis = entry_opis.get()
    lokalizacja = entry_lokalizacja.get()

    if imie == "" or wiek == "" or lokalizacja == "":
        messagebox.showwarning("Brak danych", "Uzupełnij wymagane pola")
        return
    try:
        if aktualny_typ == "klient": nowy_obiekt = klient(imie=imie, wiek=int(wiek), opis=opis, lokalizacja=lokalizacja, typ=aktualny_typ)
        else:
            nowy_obiekt = pracownik(imie=imie, wiek=int(wiek), stanowisko=opis, lokalizacja=lokalizacja)

        aktualna_lista.append(nowy_obiekt)
        pokaz_liste()

    except ValueError:
        messagebox.showerror("Błąd", "Nie udało się dodać obiektu")


def usun_obiekt() -> None:
    zaznaczenie = listbox_klienci.curselection()

    if not zaznaczenie:
        messagebox.showwarning("Brak wyboru", "Zaznacz obiekt na liście")
        return

    i = listbox_klienci.index(ACTIVE)
    aktualna_lista.pop(i)
    pokaz_liste()

def edytuj_obiekt():
    global edytowany_indeks

    zaznaczenie = listbox_klienci.curselection()

    if not zaznaczenie:
        messagebox.showwarning("Brak wyboru", "Zaznacz obiekt na liście")
        return

    i = listbox_klienci.index(ACTIVE)
    edytowany_indeks = i

    obiekt = aktualna_lista[i]

    entry_imie.delete(0, END)
    entry_wiek.delete(0, END)
    entry_opis.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.insert(0, obiekt.imie)
    entry_wiek.insert(0, obiekt.wiek)
    entry_lokalizacja.insert(0, obiekt.lokalizacja)

    if aktualny_typ == "klient":
        entry_opis.insert(0, obiekt.opis)
    else:
        entry_opis.insert(0, obiekt.stanowisko)

def pokaz_szczegoly():
    zaznaczenie = listbox_klienci.curselection()

    if not zaznaczenie:
        messagebox.showwarning("Brak wyboru", "Zaznacz obiekt na liście")
        return

    i = listbox_klienci.index(ACTIVE)
    obiekt = aktualna_lista[i]

    label_imie_wartosc.config(text=obiekt.imie)
    label_wiek_wartosc.config(text=obiekt.wiek)
    label_lokalizacja_wartosc.config(text=obiekt.lokalizacja)

    if aktualny_typ == "klient":
        label_opis_wartosc.config(text=obiekt.opis)
    else:
        label_opis_wartosc.config(text=obiekt.stanowisko)

def dodaj_randke():
    klient_randka = entry_klient_randka.get()
    osoba_randka = entry_osoba_randka.get()
    data_randka = entry_data_randka.get()

    if klient_randka == "" or osoba_randka == "" or data_randka == "":
        messagebox.showwarning("Brak danych","Uzupełnij wszystkie pola")
        return

    randki.append(randka(klient_randka, osoba_randka, data_randka))
    pokaz_randki()

    entry_klient_randka.delete(0, END)
    entry_osoba_randka.delete(0, END)
    entry_data_randka.delete(0, END)

def pokaz_randki():
    listbox_randki.delete(0, END)
    for r in randki:
        listbox_randki.insert(END, f"{r.klient} ❤ {r.osoba} | {r.data}")
