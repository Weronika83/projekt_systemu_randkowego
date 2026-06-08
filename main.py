from tkinter import *
import tkintermapview
import controller
from controller import wybierz_klientow, wybierz_pracownikow, pokaz_szczegoly, usun_obiekt, edytuj_obiekt, dodaj_obiekt, dodaj_randke, pokaz_liste, pokaz_randki

#----------------POWITANIE----------------
from powitanie import pokaz_okno_powitalne

#----------------LOGOWANIE----------------
from logowanie import pokaz_okno_logowania


# -------------------- GŁÓWNE OKNO PROGRAMU --------------------

def pokaz_program():
    global root, map_widget
    global label_lista, label_opis
    global entry_imie, entry_wiek, entry_opis, entry_lokalizacja
    global listbox_klienci, listbox_randki
    global entry_klient_randka, entry_osoba_randka, entry_data_randka
    global button_dodaj

    root = Tk()
    root.title("Portal randkowy")
    root.geometry("1100x760")

    ramka_menu = Frame(root)
    ramka_lista = Frame(root)
    ramka_formularz = Frame(root)
    ramka_szczegoly = Frame(root)
    ramka_mapa = Frame(root)
    ramka_klienci = Frame(root)

    ramka_menu.grid(row=0, column=0, sticky=N)
    ramka_lista.grid(row=1, column=0, sticky=N)
    ramka_formularz.grid(row=2, column=0, sticky=N)
    ramka_mapa.grid(row=0, column=1, rowspan=3)
    ramka_szczegoly.grid(row=3, column=0, sticky=W)
    ramka_klienci.grid(row=3, column=1, sticky=N)

    # MENU
    Label(ramka_menu, text="Wybierz moduł").grid(row=0, column=0)
    Button(ramka_menu, text="Klienci", width=25, command=wybierz_klientow).grid(row=1, column=0)
    Button(ramka_menu, text="Pracownicy", width=25, command=wybierz_pracownikow).grid(row=2, column=0)

    # LISTA
    label_lista = Label(ramka_lista, text="Lista klientów")
    label_lista.grid(row=0, column=0, columnspan=3)

    listbox_klienci = Listbox(ramka_lista, width=40, height=8)
    listbox_klienci.grid(row=1, column=0, columnspan=3)

    Button(ramka_lista, text="Pokaż", command=pokaz_szczegoly).grid(row=2, column=0)
    Button(ramka_lista, text="Usuń", command=usun_obiekt).grid(row=2, column=1)
    Button(ramka_lista, text="Edytuj", command=edytuj_obiekt).grid(row=2, column=2)

    # FORMULARZ
    Label(ramka_formularz, text="Formularz").grid(row=0, column=0, columnspan=2)

    Label(ramka_formularz, text="Imię:").grid(row=1, column=0, sticky=E)
    Label(ramka_formularz, text="Wiek:").grid(row=2, column=0, sticky=E)
    label_opis = Label(ramka_formularz, text="Opis zainteresowań:")
    label_opis.grid(row=3, column=0, sticky=E)
    Label(ramka_formularz, text="Miejscowość lub współrzędne:").grid(row=4, column=0, sticky=E)

    entry_imie = Entry(ramka_formularz)
    entry_wiek = Entry(ramka_formularz)
    entry_opis = Entry(ramka_formularz)
    entry_lokalizacja = Entry(ramka_formularz)

    entry_imie.grid(row=1, column=1)
    entry_wiek.grid(row=2, column=1)
    entry_opis.grid(row=3, column=1)
    entry_lokalizacja.grid(row=4, column=1)

    button_dodaj = Button(ramka_formularz, text="Dodaj", width=20, command=dodaj_obiekt)
    button_dodaj.grid(row=5, column=0, columnspan=2)

    # MAPA
    map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=700, height=480, corner_radius=4)
    map_widget.set_position(52.2, 21.0)
    map_widget.set_zoom(6)
    map_widget.grid(row=0, column=0)

    # SZCZEGÓŁY
    global label_imie_wartosc
    global label_wiek_wartosc
    global label_opis_wartosc
    global label_lokalizacja_wartosc

    Label(ramka_szczegoly, text="Szczegóły").grid(row=0, column=0, columnspan=2, sticky=W)

    Label(ramka_szczegoly, text="Imię:").grid(row=1, column=0, sticky=W)
    label_imie_wartosc = Label(ramka_szczegoly, text="-")
    label_imie_wartosc.grid(row=1, column=1, sticky=W)
    Label(ramka_szczegoly, text="Wiek:").grid(row=2, column=0, sticky=W)
    label_wiek_wartosc = Label(ramka_szczegoly, text="-")
    label_wiek_wartosc.grid(row=2, column=1, sticky=W)
    Label(ramka_szczegoly, text="Opis zainteresowań:").grid(row=3, column=0, sticky=W)
    label_opis_wartosc = Label(ramka_szczegoly, text="-")
    label_opis_wartosc.grid(row=3, column=1, sticky=W)
    Label(ramka_szczegoly, text="Lokalizacja:").grid(row=4, column=0, sticky=W)
    label_lokalizacja_wartosc = Label(ramka_szczegoly, text="-")
    label_lokalizacja_wartosc.grid(row=4, column=1, sticky=W)

    # RANDKI
    Label(ramka_klienci, text="Lista randek").grid(row=0, column=0, columnspan=2)
    listbox_randki = Listbox(ramka_klienci, width=45, height=7)
    listbox_randki.grid(row=1, column=0, columnspan=2)

    Label(ramka_klienci, text="Klient: ").grid(row=2, column=0)
    entry_klient_randka = Entry(ramka_klienci)
    entry_klient_randka.grid(row=2, column=1)

    Label(ramka_klienci, text="Partner: ").grid(row=3, column=0)
    entry_osoba_randka = Entry(ramka_klienci)
    entry_osoba_randka.grid(row=3, column=1)

    Label(ramka_klienci, text="Data:").grid(row=4, column=0)
    entry_data_randka = Entry(ramka_klienci)
    entry_data_randka.grid(row=4, column=1)

    Button(ramka_klienci, text="Dodaj randkę", command=dodaj_randke).grid(row=5, column=0, columnspan=2)


    controller.label_lista = label_lista
    controller.label_opis = label_opis

    controller.label_imie_wartosc = label_imie_wartosc
    controller.label_wiek_wartosc = label_wiek_wartosc
    controller.label_opis_wartosc = label_opis_wartosc
    controller.label_lokalizacja_wartosc = label_lokalizacja_wartosc

    controller.listbox_klienci = listbox_klienci
    controller.listbox_randki = listbox_randki

    controller.entry_imie = entry_imie
    controller.entry_wiek = entry_wiek
    controller.entry_opis = entry_opis
    controller.entry_lokalizacja = entry_lokalizacja

    controller.entry_klient_randka = entry_klient_randka
    controller.entry_osoba_randka = entry_osoba_randka
    controller.entry_data_randka = entry_data_randka

    controller.button_dodaj = button_dodaj
    controller.map_widget = map_widget

    pokaz_liste()
    pokaz_randki()

    root.mainloop()


if __name__ == "__main__":
    pokaz_okno_powitalne()
    pokaz_okno_logowania()