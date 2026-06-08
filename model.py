# -------------------- LISTY DANYCH --------------------
klienci = []
pracownicy = []
randki = []

#----------------DEFINIOWANIE KLAS----------------
class klient:
    def __init__(self, imie, wiek, opis, lokalizacja, typ):
        self.imie = imie
        self.wiek = wiek
        self.opis = opis
        self.lokalizacja = lokalizacja
        self.typ = typ

        self.coordinates = [52.2297, 21.0122]
        self.marker = None


class pracownik:
    def __init__(self, imie, wiek, stanowisko, lokalizacja):
        self.imie = imie
        self.wiek = wiek
        self.stanowisko = stanowisko
        self.lokalizacja = lokalizacja

        self.coordinates = [52.2297, 21.0122]
        self.marker = None


class randka:
    def __init__(self, klient, osoba, data):
        self.klient = klient
        self.osoba = osoba
        self.data = data