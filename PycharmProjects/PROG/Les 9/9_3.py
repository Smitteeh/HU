import csv

with open ('Gamers.csv', 'r') as myCSVFile:
    reader = csv.reader (myCSVFile, delimiter=';')
    scores = []
    namen = []
    datum = []

    for row in reader:
        scores.append (row[2])
        namen.append (row[0])
        datum.append (row[1])

    index = scores.index (max (scores))
    print ('De hoogste score is: ' + str (scores[index]) + ' op ' + str (datum[index]) + ' behaald door ' + str (
        namen[index]))
