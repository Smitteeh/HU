letters = ('A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C')
a= letters.count('A')
b= letters.count('B')
c= letters.count('C')
Letters = [a, b, c]
print(Letters)

cijferICOR = 7
cijferPROG = 7
cijferCSN = 7
gemiddelde = (cijferICOR + cijferPROG + cijferCSN)/3
beloning = (30*cijferICOR) + (30*cijferPROG) + (30*cijferCSN)
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + ' op!'
print(gemiddelde)
print(beloning)
print(overzicht)

print(0 == (1 == 2))
print(2 + (3 == 4) + 5 == 7)
print((1<-1)==(3>4))


uurloon = eval(input('Wat verdien je per uur?'))
aantal_uur = eval(input('Hoeveel uur heb je gewerkt?'))
salaris = uurloon * aantal_uur
print(str(aantal_uur) + ' uur werken levert ' + str(salaris) + ' Euro op')