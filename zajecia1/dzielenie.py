def suma_dzielnikow(n):
    suma = sum([i for i in range(1, n) if n % i == 0])
    return suma


def lista_dzielnikow(n):
    lista_dzielnikow = [i for i in range(1, n) if n % i == 0]
    return lista_dzielnikow
