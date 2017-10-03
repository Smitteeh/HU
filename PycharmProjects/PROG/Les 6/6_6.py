kluis_nummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
def toon_aantal_kluizen_vrij():
    with open('Kluizen.txt' ,'r') as kluizenvrij:
        aantalkluizen = len(kluizenvrij.readlines())
        vrijekluizen = 12 - aantalkluizen
        print(vrijekluizen)

def nieuwe_kluis():
    with open('Kluizen.txt', 'a') as kluizenopenen:
        wachtwoord = input('Geef een wachtwoord op:')
        kluizenopenen.writelines(str(kluis_nummers[0]) + ';' + str(wachtwoord) + '\n')
        print('Uw kluisnummer is: ' + str(kluis_nummers[0]))
        kluis_nummers.remove(kluis_nummers[0])
    return


def kluis_openen():
    with open('Kluizen.txt', 'r') as kluizen:
        kluisnummer = input ('Geef uw kluisnummer: ')
        kluiscode = input ('Geef uw kluiscode: ')
        combinatie = str(kluisnummer) + ';' + str(kluiscode)
        if combinatie in open('Kluizen.txt').read():
            print('Uw kluis is open!')
        else:
            print('Deze combinatie is niet geldig')

def kluis_teruggeven():
    with open('Kluizen.txt', 'r') as kluizen:
        kluisnummer = input ('Geef uw kluisnummer: ')
        kluiscode = input ('Geef uw kluiscode: ')
        combinatie = str (kluisnummer) + ';' + str (kluiscode)
        if combinatie in open('Kluizen.txt').read():
            kluis_nummers.append(str(kluisnummer))
    return

menu = 0
while True:
    if menu != 1:
        print ('1: Ik wil weten hoeveel kluizen nog vrij zijn')
        print ('2: Ik wil een nieuwe kluis')
        print ('3: Ik wil even iets uit mijn kluis halen')
        print ('4: Ik geef mijn kluis terug')
    menu = 1
    opdracht = input ('Maak uw keuze')
    if opdracht == 'stop':
        infile.close ()
        break
    elif opdracht == '1':
        toon_aantal_kluizen_vrij ()
    elif opdracht == '2':
        nieuwe_kluis ()
    elif opdracht == '3':
        kluis_openen ()
    elif opdracht == '4':
        kluis_teruggeven ()
    else:
        print ('U heeft geen geldig keuze gemaakt')
