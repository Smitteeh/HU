namen = []
while True:
    naam = input('Volgende naam: ')
    if naam == '':
        break
    else:
        namen.append(naam)


def aantallen(namen):
    aantal = {}
    for item in namen:
        if item in aantal:
            aantal[item] += 1
        else:
            aantal[item] = 1
    return aantal

print(aantallen(namen))

