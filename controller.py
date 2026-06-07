from model import klienci

def pokaz_liste():
    for klient in klienci:
        print(klient.imie)