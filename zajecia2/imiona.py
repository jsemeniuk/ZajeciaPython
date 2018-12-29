class NotList(Exception):
    pass


def liczba_imion(lista_imion):
    if type(lista_imion) is not list:
        raise NotList
    imiona_koniec_a = [imie for imie in lista_imion if imie[-1] == 'a']
    return len(imiona_koniec_a)


print(liczba_imion(1))
