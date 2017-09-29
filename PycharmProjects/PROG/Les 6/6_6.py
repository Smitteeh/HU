infile = open('Kluizen.txt', 'r+')
content = infile.read()
lines = infile.readlines()
def toon_aantal_kluizen_vrij():
    vrij = 12 - len(lines)
    return print(vrij)
def nieuwe_kluis():
    kluis_nummers = ['1','2','3','4','5','6','7','8','9','10','11','12']
    for nummers in kluis_nummers:
        if nummers in content:
            kluis_nummers.remove(nummers)
    if kluis_nummers == []:
        print('Er zijn helaas geen kluizen beschikbaar')
    else:
        wachtwoord = input('Geef uw code op (deze moet minimaal vier tekens bevatten)')
        infile.write(str(min(kluis_nummers)) + ';' + wachtwoord)
        print('U heeft kluis nummer: ' + str(min(kluis_nummers)))
    return
def kluis_openen():
    return
def kluis_teruggeven():
    return
menu = 0
while True:
    if menu != 1 :
        print ('1: Ik wil weten hoeveel kluizen nog vrij zijn')
        print ('2: Ik wil een nieuwe kluis')
        print ('3: Ik wil even iets uit mijn kluis halen')
        print ('4: Ik geef mijn kluis terug')
    menu = 1
    opdracht = input('Maak uw keuze')
    if opdracht == 'stop':
        infile.close ()
        break
    elif opdracht == '1':
        toon_aantal_kluizen_vrij ()
    elif opdracht == '2':
        nieuwe_kluis()
    elif opdracht == '3':
        kluis_openen()
    elif opdracht == '4':
        kluis_teruggeven()
    else:
        print('U heeft geen geldig keuze gemaakt')


