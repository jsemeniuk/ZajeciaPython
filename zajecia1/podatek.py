def podatek(kwota):
    if kwota <= 44490:
        pod = 0.19 * kwota
    elif kwota <= 85528:
        pod = 0.19*44490 + 0.3*(kwota-44490)
    else:
        pod = 0.19*44490 + 0.3*(85528-44490) + 0.4 * (kwota - 85528)
    return pod
