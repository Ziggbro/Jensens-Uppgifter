

def AdderaHundra (lista):
    summa = sum(lista)
    slutsumma = summa + 100
    return slutsumma

print(AdderaHundra([100,300,400,3]))


def HundraAddering(list):
    summa = 0
    for element in list:
        summa = summa + element
    summa = summa + 100
    return summa
print(HundraAddering([100,300,400,3]))