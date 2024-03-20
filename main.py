def wyliczPierwszyProgPodatkowy():
    #Wyliczenie dla 1 progu podatkowego:
    podatekPierwszyProg = 0
    if dochod <= 120_000:
        podatekPierwszyProg = dochod * 0.12
        print(f"Od dochodu: {dochod}\n Musisz zapłacić tyle podatku: {podatekPierwszyProg}")


def wyliczDrugiProgPodatkowy():
    if dochod >= 120_000:
        pierwszyProg = 120_000 * 0.12
        drugiProg = (dochod - 120_000) * 0.32
        print(f"Twój dochód to: {dochod}\nMusisz zapłacić podatek w "
              f"wysokości: {pierwszyProg + drugiProg}\nPodatek naliczony w I progu: {pierwszyProg}"
              f"\nPodatek naliczony w II progu podatkowym: {drugiProg}")

print("Proszę o podanie dochodu rocznego: ")
dochod = int(input())
dochod = dochod - 30_000  #Pomniejszenie o kwotę wolną od podatku
wyliczPierwszyProgPodatkowy()
wyliczDrugiProgPodatkowy()





