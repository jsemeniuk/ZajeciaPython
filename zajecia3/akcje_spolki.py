import csv


def akcje_spolki(sciezka):

    with open(sciezka, 'r') as plik_csv:
        dane = csv.reader(plik_csv, delimiter=',')

        akcje = {}

        for linia in dane:
            if len(linia) > 0:
                akcje[linia[0]] = linia[1]
    for spolka in akcje:
        print("Spolka {0}: {1}".format(spolka, akcje[spolka]))

