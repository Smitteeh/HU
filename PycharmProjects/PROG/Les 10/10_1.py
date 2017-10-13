import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

artikeldict = processXML('Artikelen.xml')
Artikelen = artikeldict['artikelen']['artikel']

for aantal in range(len(Artikelen)):
    print(Artikelen[aantal]['naam'])


