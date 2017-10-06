import csv

with open ('Accessoires.csv', 'r') as myCSVFile:
    reader = csv.reader (myCSVFile, delimiter=';')
    Artikelnummer = []
    Artikelcode = []
    Naam = []
    Voorraad = []
    Prijs = []
    Voorraadlijst = []
    for row in reader:
        Artikelnummer.append (row[0])
        Artikelcode.append (row[1])
        Naam.append (row[2])
        Voorraad.append (row[3])
        Prijs.append (row[4])

    duurste_index = Prijs.index (max (Prijs))
    minvoorrd = Voorraad.index (min (Voorraad))
    print ('Het duurste artikel is ', str (Naam[duurste_index]), ' en die kost ', str (Prijs[duurste_index]))
    print ('Er zijn slechts ', str (Voorraad[minvoorrd]), ' exemplaren in voorraad van het product met nummer ', str (
        Artikelnummer[minvoorrd]))
    Voorraad.pop (0)
    for cijfers in Voorraad:
        Voorraadlijst.append (int (cijfers))
    print ('In totaal hebben wij ', str (sum (Voorraadlijst)), ' producten in ons magazijn liggen')
