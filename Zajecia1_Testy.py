from zajecia1.bmi import *
from zajecia1.dzielenie import *
from zajecia1.klasyfikator import *
from zajecia1.kwadrat import *
from zajecia1.piramida import *
from zajecia1.podatek import *
from zajecia1.rachunek import *
from zajecia1.silnia import *
from zajecia1.VAT import *


print("Testy do zadania 1")
kwadrat(6)

print("Testy do zadania 2")
piramida(7)

print("Testy do zadania 3")
print(silnia(3))
print(silnia(5))
for i in range(3, 6):
    print("{0}: {1:4d}".format(i, suma_silni(i)))

print("Testy do zadania 4")
print(podatek(1000))
print(podatek(44490))
print(podatek(44491))
print(podatek(85528))
print(podatek(85529))

print("Testy do zadania 5")
zakupy = [0.2, 0.5, 4.59, 6]
zakupy2 = [101, 128, 55, 16]
zakupy3 = [44.35, 55.33, 23.55, 343.54, 342.55]

print(vat_faktura(zakupy))
print(vat_paragon(zakupy))

print(vat_faktura(zakupy2))
print(vat_paragon(zakupy2))

print(vat_faktura(zakupy3))
print(vat_paragon(zakupy3))

print("Testy do zadania 6")
print(suma_dzielnikow(6))

print("Testy do zadania 7")
klasyfikator("Lorem ipsum dolor sit amet, consectur adipiscing elit.")

print("Testy do zadania domowego 1")
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

print("Testy do zadania domowego 2")
print(rachunek(1))
print(rachunek(12))
print(rachunek(123))
print(rachunek(345))