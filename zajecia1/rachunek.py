"""Zadanie 2
13.11.2018, Acturis
wyk. Joanna Semeniuk
"""


def rachunek(kwota):
    portfel = [20, 10, 5, 2, 1]
    oplata = {}
    for pieniadz in portfel:
        ilosc = kwota//pieniadz
        if ilosc > 0:
            oplata[pieniadz] = ilosc
            kwota -= pieniadz * ilosc
    return oplata


print(rachunek(1))
print(rachunek(12))
print(rachunek(123))
print(rachunek(345))
