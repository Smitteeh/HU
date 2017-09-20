infile = open('Kaartnummers.txt')
content = infile.read()
print(content)

for waarden in content:
    print('{:10}{:10}{:10}{:8.2f}'.format(student[0], student[1], student[2], student[3]))





