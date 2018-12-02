def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i = i + 1
        wynik = wynik * i
    return wynik


def suma_silni(n):
    wynik = sum([silnia(i) for i in range(1, n+1)])
    return wynik
