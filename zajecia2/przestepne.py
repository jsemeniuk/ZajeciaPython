import datetime


class NotValidYear(Exception):
    pass


def przestepny(rok):
    if type(rok) is not int or rok < 1 or rok > 9999:
        raise NotValidYear
    if rok < 1582:
        return False
    return ((rok % 4 == 0) and rok % 100 != 0) or rok % 400 == 0


def nadchodzace_lp(n):
    wynik = []
    akt_rok = datetime.datetime.now().year
    while len(wynik) < n:
        if przestepny(akt_rok):
            wynik.append(akt_rok)
        akt_rok = akt_rok + 1
    return wynik
