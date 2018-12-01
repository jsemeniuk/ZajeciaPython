def suma_dzielnikow(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma


def lista_dzielnikow(n):
    lista_dzielnikow = []
    for i in range(1, n):
        if n % i == 0:
            lista_dzielnikow.append(i)
    return lista_dzielnikow


#print(suma_dzielnikow(6))

