class Uczen:
    def __init__(self, imie, nazwisko, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaOcen = oceny
        self.srednia = 0
    def dodajOcene(self, ocena):
        self.listaOcen.append(ocena)
    def wypiszDaneUcznia(self):
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

class Klasa:
    def __init__(self):
        self.listaUczniow = []

    def dodajUcznia(self):
        while True:
            listaOcen = []
            print("Podaj imię ucznia:")
            imie = input()
            print("Podaj nazwisko ucznia:")
            nazwisko = input()
            while True:
                print("Podaj Ocenę ucznia (jeśli zakończyć wciśnij x i ENTER)")
                ocena = input()
                if ocena == "x": break
                listaOcen.append(int(ocena))
            self.listaUczniow.append(Uczen(imie, nazwisko, listaOcen))
            print("Jeśli chcesz dodać kolejną osobę, kliknij ENTER. Jeśli chcesz zakończyć dodawanie ocen wciśnij x i ENTER")
            odebranaOpcja = input()
            if odebranaOpcja == "x": break
    def wyliczSredniaKlasy(self):
        suma = 0
        for uczen in self.listaUczniow:
            uczen.wyliczSredniaOcenUcznia()
            suma += uczen.srednia
        sredniaKlasy = suma / len(self.listaUczniow)
        print(f"Średnia uczniów to: {sredniaKlasy}")

    def wypiszDaneUczniow(self):
        for uczen in self.listaUczniow:
            uczen.wypiszDaneUcznia()


klasa = Klasa()
klasa.dodajUcznia()
klasa.wypiszDaneUczniow()
klasa.wyliczSredniaKlasy()