def statystyka_slow(ściezka):
    # TODO odwoływanie się bezpośrednio do plików w internecie
    stat = {}

    with open(ściezka, 'r') as fh:
        tekst = fh.read()

    for akapit in tekst.split("\n"):
        for slowo in akapit.split(" "):
            slowo = slowo.lower()
            if slowo[-1] in ".,!:;?":
                slowo = slowo[:-1]

            if slowo in stat:
                stat[slowo] += 1
            else:
                stat[slowo] = 1
    return stat

# TODO Funkcja do prównywania tekstów
def porownanie_tekstow():
    return None
