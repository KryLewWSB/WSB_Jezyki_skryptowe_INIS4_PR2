from Firma import Firma
from Kierownik import Kierownik
from Pracownik import Pracownik



firma = Firma("WSB")
firma.dodajPracownika("Anna", "Nowak", "IT", 5_500)
firma.dodajKierownika("Adam", "Kowalski", "IT", 7_500, 2_000)

firma.wypiszPracownikow()