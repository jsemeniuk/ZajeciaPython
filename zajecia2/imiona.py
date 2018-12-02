def liczba_imion(lista_imion):
    imiona_koniec_a = [imie for imie in lista_imion if imie[-1] == 'a']
    return len(imiona_koniec_a)
