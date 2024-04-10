class Pracownik:
    def __init__(self, imie, nazwisko, dzial, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dzial = dzial
        self.__wynagrodzenie = wynagrodzenie
    def getWynagrodzenie(self):
        return self.__wynagrodzenie
    def wypiszPersonalia(self):
        print(f"Imię pracownika: {self.imie}\nNazwisko pracownika: {self.nazwisko}"
              f"\nDzial pracownika: {self.dzial}\nWynagrodzenie pracownika: {self.__wynagrodzenie} zł.")