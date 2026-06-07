from model import klienci

def pokaz_liste():
    for klient in klienci:
        print(klient.imie)

def wybierz_klientow():
    print("Wybrano moduł klienci")

def wybierz_pracownikow():
    print("Wybrano moduł pracownicy")