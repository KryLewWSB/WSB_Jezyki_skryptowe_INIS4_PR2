

while True:
    print("Proszę o podanie liczby: ")
    pobranaLiczba = int(input())
    if pobranaLiczba % 2 == 0:
        print(f"{pobranaLiczba} - ta liczba jest parzysta!")
    else:
        print(f"{pobranaLiczba} - ta liczba  jest NIE parzysta!")
    print("Jeśli zakończyć wpisz \"x\" i ENTER, jeśli liczyć dalej wpisz samo ENTER")
    podanaWartosc = input()
    if podanaWartosc == "x":
        break