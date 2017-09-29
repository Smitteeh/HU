Woord = []
while True:
    woordje = input('Geef een string van vier letters: ')
    if len(woordje) == 4:
        print('Inlezen van correcte string: ' + str(woordje) + ' is geslaagd!')
        break
    else:
        print(str(woordje) + ' heeft ' + str(len(woordje)) + ' letters')