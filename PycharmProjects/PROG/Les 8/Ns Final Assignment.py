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


def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation ' + str(beginstation))


beginstation = inlezen_beginstation (stations)
eindstation = inlezen_eindstation (stations, beginstation)
omroepen_reis (stations, beginstation, eindstation)
