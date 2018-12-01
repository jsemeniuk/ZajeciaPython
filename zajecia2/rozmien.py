"""Zadanie 1
20.11.2018, Acturis
wyk. Joanna Semeniuk
"""


def rozmien(portfel, kwota):
    oplata = {}
    dl_portfel = len(portfel)
    while dl_portfel > 1:
        dl_portfel -= 1
        if portfel[dl_portfel] > 0:
            ilosc = kwota//dl_portfel
            if ilosc > 0:
                if ilosc <= portfel[dl_portfel]:
                    oplata[dl_portfel] = ilosc
                    kwota -= dl_portfel * ilosc
                elif ilosc > portfel[dl_portfel]:
                    oplata[dl_portfel] = portfel[dl_portfel]
                    kwota -= dl_portfel * portfel[dl_portfel]
    if kwota > 0:
        oplata['pozostalakwota'] = kwota
    return oplata


portfel_test = [0, 2, 3, 0, 0, 5]
kwota_test = 34


print(rozmien(portfel_test, kwota_test))
