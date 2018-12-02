"""Zadanie 1
13.11.2018, Acturis,
wyk. Joanna Semeniuk
"""


def bmi(masa, wzrost):
    if masa > 0 and wzrost > 0:
        return round(masa / (wzrost ** 2), 1)
    else:
        return "Podane wartości są nieprawidłowe"


def komentarz(bmi):
    if bmi < 18.5:
        return "Bmi równe %s oznacza: niedowagę" % bmi
    elif bmi < 24.9:
        return "Bmi równe %s oznacza: wagę prawidłową" % bmi
    elif bmi < 30:
        return "Bmi równe %s oznacza: nadwagę" % bmi
    elif bmi >= 30:
        return "Bmi równe %s oznacza: otyłość" % bmi




