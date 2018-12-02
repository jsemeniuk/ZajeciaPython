from zajecia2.dzielniki import *
from zajecia2.funkcja_ackermanna import *
from zajecia2.imiona import *
from zajecia2.liczby_pierwsze import *
from zajecia2.odsetki import *
from zajecia2.palindrom import *
from zajecia2.przestepne import *
from zajecia2.rozmien import *
from zajecia2.zdania import *

print("Testy do zadania 1")
print(a(1, 1))
print(a(0, 2))
print(a(2, 0))
print(a(3, 3))

print("Testy do zadania 2")
print(odsetki(0.03, 12, 1000))
print(lokata_odnawialna(0.03, 3, 1000))

print("Testy do zadania 4")
test = [1, 3, 4, 8, 11, 44]
for liczba in test:
    print("{0}: {1}".format(str(liczba), pierwsza(liczba)))

print("Testy do zadania 5")
print(dzielniki_pierwsze(12))
print(doskonala(12))

print("Testy do zadania 6")
lista_imion = ['Tomek', 'Stefan', 'Gustaw', 'Eufrozyna', 'Antonina', 'Marian', 'Antoni', 'Aleksandra', 'Julia']
print(liczba_imion(lista_imion))

print("Testy do zadania 7")
lista = [["lódź", "się", "obudziła"], ["ogary", "poszły", "w", "las"]]
print(zbuduj_zdania(lista))

print("Testy do zadania 8")
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(uprosc_zdanie(tekst, 9, 5))

print("Testy do zadania z palindromami")
dane = ['kajak', 'kobylamamalybok', 'palindrom', [1, 2, 1], [2, 3]]
wersje = [wer1, wer2]

for funkcja in wersje:
    for slowo in dane:
        print("{0}: {1}".format(slowo, funkcja(slowo)))

print("Testy do zadania z latami przestępnymi")
print(nadchodzace_lp(4))

print("Testy do zadania domowego 1")
portfel_test = [0, 2, 3, 0, 0, 5]
kwota_test = 34

print(rozmien(portfel_test, kwota_test))