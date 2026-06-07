from model import klienci, klient


def wybierz_klientow():
    print("Wybrano moduł klienci")

def wybierz_pracownikow():
    print("Wybrano moduł pracownicy")


# -------------------- LISTA --------------------
def pokaz_liste():
    for klient in klienci:
        print(klient.imie)


#----------------DODAWANIE, USUWANIE, EDYTOWANIE----------------
def dodaj_obiekt(imie, wiek, opis, lokalizacja):
    nowy_klient = klient(
        imie,
        int(wiek),
        opis,
        lokalizacja,
        "klient"
    )

    klienci.append(nowy_klient)