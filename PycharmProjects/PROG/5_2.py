infile = open('Kaartnummers.txt')
content = infile.read()
gesplit = content.split()
print(gesplit)
def i(nummer):
    res = gesplit[nummer] + ' '
    return res
rest = 'heeft kaartnummer: '

print(i(1) + i(2) + rest + i(3))
print(i(4) + i(5) + rest + i(6))
print(i(7) + i(8) + rest + i(9))
print(i(10) + i(11) + rest + i(12))

