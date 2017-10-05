import csv
import time

# bestand = 'inloggers.csv' #gebruik hier een herhalingslus:
# naam = input("Wat is je achternaam? ")
# voorl = input("Wat zijn je voorletters? ")
# gbdatum = input("Wat is je geboortedatum? ")
# email = input("Wat is je e-mail adres? ")
# wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file

with open ('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer (myCSVFile, delimiter=';')
    writer.writerow (('Datum', 'Voorletters', 'Achternaam', 'Geboortedatum', 'E-mail adres'))

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == '':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        datum = time.strftime ('%A %b/%d/%y %I:%M', time.localtime ())

        writer.writerow ((datum,voorl, naam, gbdatum, email))
