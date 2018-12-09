class Wyrazenie:
    pass


class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

    def uprosc(self):
        return self.lewy + self.prawy


class Stala(Wyrazenie):

    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return str(self.wartosc)

    def __add__(self, other):
        return self.wartosc + other.wartosc


class Mnozenie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " * " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) * self.prawy.oblicz(stan)


class Rownosc(Wyrazenie):
    # TODO Dodać funkcja rozwiąz
    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " = " + str(self.prawy)


wyrazenie = Rownosc(Dodawanie(Zmienna("x"), Zmienna("y")), Stala(4))
print(wyrazenie)

