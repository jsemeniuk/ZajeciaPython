def vat_faktura(lista):
    suma = sum([element for element in lista])
    vat = round(0.23*suma, 2)
    return vat


def vat_paragon(lista):
    vat = sum([round(0.23*element, 2) for element in lista])
    return round(vat, 2)
