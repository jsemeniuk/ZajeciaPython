from zajecia1.VAT import vat_paragon


def zakupy(cennik, lista):
    paragon = []
    for element in lista:
        if element in cennik:
            paragon.append(cennik[element] * lista[element])
    # Zwraca tylko vat - poprawić
    rachunek = vat_paragon(paragon)
    return rachunek


cennik = {
    'kawa' : 14.99,
    'pomarańcze' : 3.49,
    'olej' : 4.99
}

lista = {'olej' : 2, 'kawa' : 1}

print(zakupy(cennik, lista))
