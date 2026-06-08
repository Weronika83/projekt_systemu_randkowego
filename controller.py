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
map_widget = None

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
    wyczysc_formularz()

def wybierz_pracownikow():
    global aktualna_lista, aktualny_typ, edytowany_indeks
    aktualna_lista = pracownicy
    aktualny_typ = "pracownik"
    edytowany_indeks = None
    label_lista.config(text="Lista pracowników")
    label_opis.config(text="Stanowisko:")

    pokaz_liste()
    wyczysc_formularz()

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
        if aktualny_typ == "klient":
            nowy_obiekt = klient(imie=imie, wiek=int(wiek), opis=opis, lokalizacja=lokalizacja, typ=aktualny_typ)
        else:
            nowy_obiekt = pracownik(imie=imie, wiek=int(wiek), stanowisko=opis, lokalizacja=lokalizacja)

        aktualna_lista.append(nowy_obiekt)
        nowy_obiekt.marker = map_widget.set_marker( nowy_obiekt.coordinates[0], nowy_obiekt.coordinates[1], text=nowy_obiekt.imie)

        pokaz_liste()
        wyczysc_formularz()
    except ValueError:
        messagebox.showerror("Błąd", "Nie udało się dodać obiektu")

def usun_obiekt() -> None:
    zaznaczenie = listbox_klienci.curselection()
    if not zaznaczenie:
        messagebox.showwarning("Brak wyboru", "Zaznacz obiekt na liście")
        return

    i = listbox_klienci.index(ACTIVE)
    if aktualna_lista[i].marker:
        aktualna_lista[i].marker.delete()
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
    wyczysc_formularz()

    entry_imie.insert(0, obiekt.imie)
    entry_wiek.insert(0, obiekt.wiek)
    entry_lokalizacja.insert(0, obiekt.lokalizacja)

    if aktualny_typ == "klient":
        entry_opis.insert(0, obiekt.opis)
    else:
        entry_opis.insert(0, obiekt.stanowisko)

    button_dodaj.config(text="Zapisz zmiany", command=zapisz_zmiany)

def zapisz_zmiany():
    global edytowany_indeks
    if edytowany_indeks is None: return
    i = edytowany_indeks
    aktualna_lista[i].imie = entry_imie.get()
    aktualna_lista[i].wiek = int(entry_wiek.get())
    aktualna_lista[i].lokalizacja = entry_lokalizacja.get()
    if aktualny_typ == "klient":
        aktualna_lista[i].opis = entry_opis.get()
    else:
        aktualna_lista[i].stanowisko = entry_opis.get()

    if aktualna_lista[i].marker:
        aktualna_lista[i].marker.delete()

    aktualna_lista[i].marker = map_widget.set_marker(aktualna_lista[i].coordinates[0], aktualna_lista[i].coordinates[1], text=aktualna_lista[i].imie)

    button_dodaj.config(text="Dodaj", command=dodaj_obiekt)
    edytowany_indeks = None

    wyczysc_formularz()
    pokaz_liste()

def pokaz_szczegoly():
    if not listbox_klienci.curselection():
        return
    i = listbox_klienci.index(ACTIVE)
    imie = aktualna_lista[i].imie
    wiek = aktualna_lista[i].wiek
    lokalizacja = aktualna_lista[i].lokalizacja

    label_imie_wartosc.config(text=imie)
    label_wiek_wartosc.config(text=wiek)
    label_lokalizacja_wartosc.config(text=lokalizacja)

    if aktualny_typ == "klient":
        label_opis_wartosc.config(text=aktualna_lista[i].opis)
    else:
        label_opis_wartosc.config(text=aktualna_lista[i].stanowisko)

    map_widget.set_position(aktualna_lista[i].coordinates[0], aktualna_lista[i].coordinates[1])
    map_widget.set_zoom(12)

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

def wyczysc_formularz():
    entry_imie.delete(0, END)
    entry_wiek.delete(0, END)
    entry_opis.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.focus()