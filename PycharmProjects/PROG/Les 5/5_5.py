def gemiddelde(zin):
    outfile = open('Zin.txt', 'r+')
    outfile.write(zin)
    outfile.close()
    infile = open('Zin/txt', 'r+')
    content = infile.read()
    woorden = content.split()
    print(woorden)

gemiddelde('Hallo ik ben Chris')






