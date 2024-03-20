class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaOcen = []
        self.srednia = 0
    def dodajOcene(self, ocena):
        self.listaOcen.append(ocena)
    def wypiszDAneUcznia(self):
        print(f"Imię ucznia: {self.imie} | Nazwisko ucznia: {self.nazwisko} | "
              f"Oceny ucznia: {self.listaOcen}")
    def wyliczSredniaOcenUcznia(self):
        sumaOcen = 0
        #Robimy sumowanie w pętli wszystkich ocen:
        for i in self.listaOcen:
            sumaOcen += i
        #Sumę ocen dzielimy przez ilosc ocen
        srednia = sumaOcen / len(self.listaOcen)
        print(f"Średnia ocen ucznia {self.imie} {self.nazwisko} to: {srednia}")

uczen = Uczen("Adam", "Kowal")
uczen.dodajOcene(5)
uczen.dodajOcene(5)
uczen.dodajOcene(4)
uczen.dodajOcene(3)

uczen.wyliczSredniaOcenUcznia()