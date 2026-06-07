klienci = []
pracownicy = []
randki = []

class klient:
    def __init__(self, imie, wiek, opis, lokalizacja, typ):
        self.imie = imie
        self.wiek = wiek
        self.opis = opis
        self.lokalizacja = lokalizacja
        self.typ = typ

class pracownik:
    def __init__(self, imie, wiek, stanowisko, lokalizacja):
        self.imie = imie
        self.wiek = wiek
        self.stanowisko = stanowisko
        self.lokalizacja = lokalizacja

class randka:
    def __init__(self, klient, osoba, data):
        self.klient = klient
        self.osoba = osoba
        self.data = data