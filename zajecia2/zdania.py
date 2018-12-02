import random


def zbuduj_zdania(lista):
    zdanie = ""
    for lista_zdanie in lista:
        zdanie += zbuduj_zdanie(lista_zdanie)
    return zdanie


def zbuduj_zdanie(lista):
    zdanie = ""
    lista[0] = lista[0].capitalize()
    if lista[-1][-1] != '.':
        lista[-1] = lista[-1] + '.'
    for slowo in lista:
        zdanie += slowo + ' '
    return zdanie


def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    lista_slow = []
    for slowo in tekst.split(" "):
        if len(slowo) <= dl_slowa:
            lista_slow.append(slowo)
    slowa_do_usuniecia = len(lista_slow) - liczba_slow
    for i in range(slowa_do_usuniecia):
        losowy_wyraz = random.randint(0, len(lista_slow) - 1)
        lista_slow.pop(losowy_wyraz)
    return zbuduj_zdanie(lista_slow)
