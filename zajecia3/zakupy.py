from zajecia1.VAT import vat_paragon


def zakupy(cennik, lista):
    paragon = []
    rachunek_bez_vat = 0
    for element in lista:
        if element in cennik:
            paragon.append(cennik[element] * lista[element])
            rachunek_bez_vat += cennik[element] * lista[element]
    vat = vat_paragon(paragon)
    rachunek = rachunek_bez_vat + vat
    return rachunek
