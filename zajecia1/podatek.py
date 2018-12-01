def podatek(kwota):
    if kwota <= 44490:
        pod = 0.19 * kwota
    elif kwota <= 85528:
        pod = 0.19*44490 + 0.3*(kwota-44490)
    else:
        pod = 0.19*44490 + 0.3*(85528-44490) + 0.4 * (kwota - 85528)
    return pod


print(podatek(1000))
print(podatek(44490))
print(podatek(44491))
print(podatek(85528))
print(podatek(85529))
