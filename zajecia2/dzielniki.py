from zajecia1.dzielenie import *
from liczby_pierwsze import pierwsza


def dzielniki_pierwsze(n):
    lista_dzielnikow_pierwszych = []
    for dzielnik in lista_dzielnikow(n):
        if pierwsza(dzielnik):
            lista_dzielnikow_pierwszych.append(dzielnik)
    return lista_dzielnikow_pierwszych


def doskonala(n):
    suma = 0
    for dzielnik in dzielniki_pierwsze(n):
        suma += dzielnik
    if suma == n:
        return True
    else:
        return False


print(dzielniki_pierwsze(12))
print(doskonala(12))
