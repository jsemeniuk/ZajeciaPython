from zajecia3.przegladanie import *
from zajecia3.statystyka import *
from zajecia3.statystyka_slow import *
from zajecia3.zakupy import *


print("Testy do zadania 1")
cennik = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
}

lista = {'olej': 2, 'kawa': 1}

print(zakupy(cennik, lista))
print("Testy do zadania 2")
print(przegladanie('zajecia3'))

print("Testy do zadania 3")
print(statystyka('zajecia3/plik_testowy'))

print("Testy do zadania domowego 1")
print(statystyka_slow('zajecia3/plik_testowy'))
