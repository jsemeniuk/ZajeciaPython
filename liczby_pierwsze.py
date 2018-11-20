from dzielenie import lista_dzielnikow

def pierwsza(n):
    for dzielnik in lista_dzielnikow(n):
        if dzielnik != 1:
            return False
    return True


test = [1, 3, 4, 8, 11, 44]
for liczba in test:
    print("{0}: {1}".format(str(liczba), pierwsza(liczba)))

