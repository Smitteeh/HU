stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']

def inlezen_beginstation(stations):
    while True:
        station = input ('Geef uw beginstation: ')
        if station in stations:
            beginstation = station
            break
        else:
            print ('Deze trein komt niet in ' + str (station))
    return station

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input ('Geef uw eindstation: ')
        if eindstation in stations:
            index_begin = stations.index (beginstation)
            index_eindstation = stations.index (eindstation)
            if index_begin < index_eindstation:
                break
            else:
                print ('Dit station ligt niet op het komende traject')
        else:
            print ('Dit station ligt niet op het traject')
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    afstand = stations.index (eindstation) - stations.index (beginstation)
    print ('Het beginstation ' + str (beginstation) + ' is het ' + str (stations.index (beginstation) + 1) + 'e station in het traject.')
    print ('Het eindstation ' + str (eindstation) + ' is het ' + str (stations.index (eindstation) + 1) + 'e station in het traject.')
    print ('De afstand bedraagt ' + str (afstand) + ' station(s)')
    print ('De prijs van een kaartje bedraagt: ' + str (afstand * 5) + ' Euro.')
    print ('Jij stapt in de trein in: ' + str (beginstation))
    for station in stations:
        if stations.index (station) > stations.index (beginstation) and stations.index (station) < stations.index (
                eindstation):
            print (' -' + str (station))
    print ('Jij stapt uit in: ' + str (eindstation))

beginstation = inlezen_beginstation (stations)
eindstation = inlezen_eindstation (stations, beginstation)
omroepen_reis (stations, beginstation, eindstation)
