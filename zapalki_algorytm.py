"""Zadanie 2 - Algorytm
20.11.2018, Acturis
wyk. Joanna Semeniuk
"""
import random


def losuj_zapalki():
    ilosc_zapalek = random.randint(7, 100)
    return ilosc_zapalek


def zapalki_walidacja():
    while True:
        zabrane_zapalki = input('Zabierz 1, 2 lub 3 zapałki: ')
        try:
            zabrane_zapalki = int(zabrane_zapalki)
            if (zabrane_zapalki == 1 or
                zabrane_zapalki == 2 or
                zabrane_zapalki == 3):
                return zabrane_zapalki
            else:
                print('Podana wartość jest nieprawidłowa')
        except ValueError:
            print('Podana wartość jest nieprawidłowa')


def zapalki_gracz(ilosc_zapalek, zabrane_zapalki):
    ilosc_zapalek -= zabrane_zapalki
    if ilosc_zapalek == 1:
        print('Komputer zabiera ostatnią zapałkę')
        print('Gratulacje! Wygrałeś!')
    elif ilosc_zapalek > 1:
        print('Ilość zapałek po zabraniu przez gracza: %s' % ilosc_zapalek)
    else:
        print('Zabrałeś ostatnią zapałkę')
        print('Przegrałeś')
    return ilosc_zapalek


def zapalki_komputer(ilosc_zapalek):
    zabrane_zapalki = random.randint(1, 3)
    if ilosc_zapalek - zabrane_zapalki <= 0:
        zabrane_zapalki = 1
    print('Zapałki zabrane przez komputer: %s' % zabrane_zapalki)
    ilosc_zapalek -= zabrane_zapalki
    if ilosc_zapalek == 1:
        print('Została Ci ostatnia zapałka do zabrania')
        print('Przegrałeś')
    elif ilosc_zapalek > 1:
        print('Ilość zapałek po zabraniu przez komputer: %s' % ilosc_zapalek)
    else:
        print('Komputer zabrał ostatnią zapałkę')
        print('Gratulacje! Wygrałeś!')
    return ilosc_zapalek
