import requests
from bs4 import BeautifulSoup

# -------------------- LISTY DANYCH --------------------
klienci = []
pracownicy = []
randki = []

#----------------DEFINIOWANIE KLAS----------------
class klient:
    def __init__(self, imie: str, wiek: int, opis: str, lokalizacja: str, typ: str):
        self.imie = imie
        self.wiek = wiek
        self.opis = opis
        self.lokalizacja = lokalizacja
        self.typ = typ

        self.coordinates = self.get_coordinates()
        self.marker = None

    def get_coordinates(self) -> list:
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.lokalizacja}"
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response_html = BeautifulSoup(response.text, 'html.parser')
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            return [latitude, longitude]

        except:
            return [52.2297, 21.0122]

class pracownik:
    def __init__(self, imie, wiek, stanowisko, lokalizacja):
        self.imie = imie
        self.wiek = wiek
        self.stanowisko = stanowisko
        self.lokalizacja = lokalizacja

        self.coordinates = self.get_coordinates()
        self.marker = None

    def get_coordinates(self) -> list:
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.lokalizacja}"
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response_html = BeautifulSoup(response.text, 'html.parser')
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            return [latitude, longitude]

        except:
            return [52.2297, 21.0122]

class randka:
    def __init__(self, klient, osoba, data):
        self.klient = klient
        self.osoba = osoba
        self.data = data
