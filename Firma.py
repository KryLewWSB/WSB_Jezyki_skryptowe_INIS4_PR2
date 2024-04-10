from Kierownik import Kierownik
from Pracownik import Pracownik

class Firma:
    __listaPracownikow = []
    def __init__(self, name):
        self.name = name
    def dodajPracownika(self, imie, nazwisko, dzial, wynagrodzenie):
        self.__listaPracownikow.append(Pracownik(imie, nazwisko, dzial, wynagrodzenie))
    def dodajKierownika(self, imie, nazwisko, dzial, wynagrodzenie, premia):
        self.__listaPracownikow.append(Kierownik(imie, nazwisko, dzial, wynagrodzenie, premia))
    def wypiszPracownikow(self):
        for pracownik in self.__listaPracownikow:
            pracownik.wypiszPersonalia()