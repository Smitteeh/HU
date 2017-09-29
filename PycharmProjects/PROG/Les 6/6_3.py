invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
Lijst = []
for waarde in invoer:
    if waarde != '-':
        Lijst.append(int(waarde))
Lijst.sort()
print('Geimporteerde lijst van ints: ' + str(Lijst))
print('Grootste getal: ' + str(max(Lijst)) + ' en Kleinste getal: ' + str(min(Lijst)))
print('Aantal getallen: ' + str(len(Lijst))+ ' en de som van de getallen: '+ str(sum(Lijst)))
print('Gemiddelde: ' + str(sum(Lijst)/len(Lijst)))
