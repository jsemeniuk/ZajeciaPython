import re


class NotString(Exception):
    pass


def statystyka(sciezka):
    if type(sciezka) is not str:
        raise NotString

    stat = {}
    try:
        with open(sciezka, 'r') as fh:
            tekst = fh.read()
        stat['Liczba znaków'] = liczba_znakow(tekst)
        stat['Liczba słów'] = liczba_slow(tekst)
        stat['Liczba zdan'] = liczba_zdan(tekst)

        return stat
    except FileNotFoundError:
        print("Niewłaściwa ścieżka do pliku")


def liczba_znakow(tekst):
    liczba_znakow = sum([1 for znak in tekst if znak != ' '])
    return liczba_znakow


def liczba_slow(tekst):
    liczba_slow = sum([len(akapit.split(" ")) for akapit in tekst.split("\n")])
    return liczba_slow


def liczba_zdan(tekst):
    liczba_zdan = sum([1 for zdanie in re.split("[.!?]", tekst) if len(zdanie) > 0])
    return liczba_zdan


print(statystyka('test'))