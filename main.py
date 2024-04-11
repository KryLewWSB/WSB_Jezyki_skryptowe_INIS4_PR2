from ETypKlienta import ETypKlienta
from Firma import Firma
from Kierownik import Kierownik
from Klient import Klient
from Pracownik import Pracownik



firma = Firma("WSB")
firma.dodajPracownika("Anna", "Nowak", "IT", 5_500)
firma.dodajKierownika("Adam", "Kowalski", "IT", 7_500, 2_000)

firma.wypiszPracownikow()

klient1 = Klient("Adam", "Nowak", ETypKlienta.INDYWIDUALNY)
klient1.wypiszPersonalia()
