"""Zadanie 2 - Interakcja z graczem
20.11.2018, Acturis
wyk. Joanna Semeniuk
"""
from zapalki_algorytm import *

ilosc_zapalek = losuj_zapalki()
print('Początkowa ilość zapałek: %s' % ilosc_zapalek)
gracz = True
komputer = False
while ilosc_zapalek > 1:
    if gracz:
        zabrane_zapalki = zapalki_walidacja()
        ilosc_zapalek = zapalki_gracz(ilosc_zapalek, zabrane_zapalki)
        gracz = False
        komputer = True
    elif komputer:
        ilosc_zapalek = zapalki_komputer(ilosc_zapalek)
        komputer = False
        gracz = True
