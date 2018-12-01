def statystyka(ściezka):
    stat = {}

    with open(ściezka, 'r') as fh:
        tekst = fh.read()

    stat['Liczba znaków'] = liczba_znakow(tekst)
    stat['Liczba słów'] = liczba_slow(tekst)
    stat['Liczba zdan'] = liczba_zdan(tekst)
    return stat


def liczba_znakow(tekst):
    liczba_znakow = 0
    for znak in tekst:
        if znak != ' ':
            liczba_znakow += 1
    return liczba_znakow


def liczba_slow(tekst):
    liczba_slow = 0
    for akapit in tekst.split("\n"):
        liczba_slow += len(akapit.split(" "))
    return liczba_slow


def liczba_zdan(tekst):
    liczba_zdan = 0
    for zdanie in tekst.split("."):
        if len(zdanie) > 0:
            liczba_zdan += 1
    return liczba_zdan


print(statystyka('plik_testowy'))