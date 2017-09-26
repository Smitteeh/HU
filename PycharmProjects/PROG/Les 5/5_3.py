infile = open('Kaartnummers.txt', 'r')
content = infile.readlines()
infile.close()

infile = open('Kaartnummers.txt', 'r')
Nummer = infile.read()
Woorden = Nummer.split()
nummers = []
for i in Woorden:
    if i.isdigit():
        nummers.append(i)

print('Deze file heeft ' + str(len(content)) + ' lines.')
print('Het grootste kaartnummer is: ' + str(max(nummers)))
