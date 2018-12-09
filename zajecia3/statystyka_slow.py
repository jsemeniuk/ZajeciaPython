def statystyka_slow(sciezka):
    # TODO odwoływanie się bezpośrednio do plików w internecie
    stat = {}

    with open(sciezka, 'r', encoding='utf-8') as fh:
        tekst = fh.read()
        for akapit in tekst.split("\n"):
            if len(akapit) > 0:
                for slowo in akapit.split(" "):
                    slowo = slowo.lower()
                    if len(slowo) > 1 and slowo[-1] in ['.', ',',  '!', ':', ';', '?', '...']:
                        slowo = slowo[:-1]

                    if slowo in stat:
                        stat[slowo] += 1
                    else:
                        stat[slowo] = 1

    return stat


def porownanie_tekstow(sciezka1, sciezka2):
    statystyka_tekstu1 = statystyka_slow(sciezka1)
    statystyka_tekstu2 = statystyka_slow(sciezka2)
    slowa_tylko_w_tekst1 = [slowo for slowo in statystyka_tekstu1 if slowo not in statystyka_tekstu2]
    slowa_tylko_w_tekst2 = [slowo for slowo in statystyka_tekstu2 if slowo not in statystyka_tekstu1]
    print(slowa_tylko_w_tekst1)
    print(slowa_tylko_w_tekst2)
    roznica_slow = {}
    for slowo in statystyka_tekstu1:
        if slowo in statystyka_tekstu2:
            roznica_slow[slowo] = abs(statystyka_tekstu1[slowo] - statystyka_tekstu2[slowo])
    print(roznica_slow)
