def gemiddelde(zin):
    outfile = open('Zin.txt', 'r+')
    outfile.write(zin)
    outfile.close()
    infile = open('Zin.txt', 'r+')
    content = infile.read()
    woorden = content.split()
    aantal_woorden = len(woorden)
    lengte_zin = len(content)
    print(zin)
    print('Het gemiddelde aantal letters per woord in deze zin is: ' + str(lengte_zin / aantal_woorden))

gemiddelde('Hallo ik ben Chris')






