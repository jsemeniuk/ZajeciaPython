from zajecia1.bmi import bmi


class Osoba:

    def __init__(self, imie, nazwisko, waga=1, wzrost=1):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost

    def __str__(self):
        return self.__class__.__name__ + ": " + self.imie + " " + self.nazwisko

    def bmi(self):
        return bmi(self.waga, self.wzrost)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, waga=1, wzrost=1):
        Osoba.__init__(self, imie, nazwisko, waga, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2


class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0


o = Osoba("Jan",  "Kowalski", 50, 1.67)
print(o)
print(o.bmi())

p = Pracownik("Jan", "Nowak", 2250, 50, 1.67)
print("{0} wypłata {1}".format(p, p.wyplata()))
print(p.bmi())

k = Kierownik("Anna", "",  5000, 50, 1.67)
print(k.wyplata())
print(k.bmi())