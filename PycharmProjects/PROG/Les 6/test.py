infile = open('Kluizen.txt', 'r+')
context = infile.read()
kluis_nummers = ['1','2','3','4','5','6','7','8','9','10','11','12']

for nummers in kluis_nummers:
    if nummers in context:
        kluis_nummers.remove(nummers)

print(kluis_nummers)