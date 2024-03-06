print("Proszę o podanie liczby: ")
pobranaLiczba = int(input())

try:
    if pobranaLiczba % 2 == 0:
        print(f"{pobranaLiczba} - ta liczba jest parzysta!")
    else:
        print(f"{pobranaLiczba} - ta liczba  jest NIE parzysta!")
except:
    print("Pojawił się błąd")