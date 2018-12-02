def wer1(slowo):
    for i in range(len(slowo)):
        if slowo[i] != slowo[-1-i]:
            return False
    return True


def wer2(slowo):
    return slowo == slowo[::-1]
