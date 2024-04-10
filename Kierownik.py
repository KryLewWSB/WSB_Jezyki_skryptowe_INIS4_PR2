from Pracownik import Pracownik

class Kierownik(Pracownik):
    def __init__(self, imie, nazwisko, dzial, wynagrodzenie, premiaKierownicza):
        super().__init__(imie, nazwisko, dzial, wynagrodzenie)
        self.__premiaKierownicza = premiaKierownicza
    def wypiszPersonalia(self):
        print(f"Imię pracownika: {self.imie}\nNazwisko pracownika: {self.nazwisko}"
              f"\nDzial pracownika: {self.dzial}\nWynagrodzenie pracownika: {self.getWynagrodzenie()} zł"
              f"\nPremia Kierownicza: {self.__premiaKierownicza} zł.")