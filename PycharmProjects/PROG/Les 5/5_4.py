import time
print(time.strftime('%A %b/%d/%y %I:%M %p', time.localtime()))

outfile = open('Hardlopers.txt', 'r+')
Naam = ''
while True:
    Naam = input ('Naam')
    if Naam == 'Stop' or Naam == 'stop':
        break
    outfile.write (str(time.strftime ('%A %b/%d/%y %I:%M %p', time.localtime ())) + ' ' + Naam + '\n')

outfile.close()

infile = open('Hardlopers.txt', 'r')
for line in infile:
    print(line,end='')

infile.close()
