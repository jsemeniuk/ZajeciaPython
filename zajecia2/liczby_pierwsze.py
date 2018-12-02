from zajecia1.dzielenie import lista_dzielnikow

def pierwsza(n):
    for dzielnik in lista_dzielnikow(n):
        if dzielnik != 1:
            return False
    return True
