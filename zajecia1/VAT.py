def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat


def vat_paragon(lista):
    vat = 0
    for element in lista:
        vat += round(0.23*element, 2)
    return round(vat, 2)


# zakupy = [0.2, 0.5, 4.59, 6]
# zakupy2 = [101, 128, 55, 16]
# zakupy3 = [44.35, 55.33, 23.55, 343.54, 342.55]

# print(vat_faktura(zakupy))
# print(vat_paragon(zakupy))

# print(vat_faktura(zakupy2))
# print(vat_paragon(zakupy2))

# print(vat_faktura(zakupy3))
# print(vat_paragon(zakupy3))