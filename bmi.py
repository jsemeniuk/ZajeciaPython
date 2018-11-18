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


bmi0 = bmi(0, 0)
print(bmi0)

bmi1 = bmi(41.40, 1.50)
print(komentarz(bmi1))

bmi2 = bmi(51.59, 1.67)
print(komentarz(bmi2))

bmi3 = bmi(62, 1.53)
print(komentarz(bmi3))

bmi4 = bmi(100, 1.50)
print(komentarz(bmi4))

