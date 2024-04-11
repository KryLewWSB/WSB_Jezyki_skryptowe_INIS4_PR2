from IWypiszDane import IWypiszDane

class Klient(IWypiszDane):
    def __init__(self, imie, nazwisko, typKlienta):
        self.imie = imie
        self.nazwisko = nazwisko
        self.typKlienta = typKlienta
    def wypiszPersonalia(self):
        print(f"Imię: {self.imie}\nNazwisko: {self.nazwisko}\nTypKlienta: {self.typKlienta}")
