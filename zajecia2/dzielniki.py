from zajecia1.dzielenie import *
from zajecia2.liczby_pierwsze import pierwsza


def dzielniki_pierwsze(n):
    lista_dzielnikow_pierwszych = [dzielnik for dzielnik in lista_dzielnikow(n) if pierwsza(dzielnik)]
    return lista_dzielnikow_pierwszych


def doskonala(n):
    suma = sum([dzielnik for dzielnik in dzielniki_pierwsze(n)])
    if suma == n:
        return True
    else:
        return False
