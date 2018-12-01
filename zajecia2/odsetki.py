def odsetki(oproc, czas, kwota):
    wynik = kwota * oproc * (czas / 12)
    return wynik


def lokata_odnawialna(oproc, czas, kwota):
    ile = int(12/czas)
    ods_wynik = 0
    for i in range(ile):
        odsetki = kwota * oproc * (czas / 12)
        kwota += odsetki
        ods_wynik += odsetki
    return ods_wynik


print(odsetki(0.03, 12, 1000))
print(lokata_odnawialna(0.03, 3, 1000))
