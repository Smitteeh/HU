import xmltodict
with open ("stations.xml",'r') as myXMLFile :
    file = myXMLFile.read()
    xmldictionary = xmltodict.parse(file)
    stations = xmldictionary['Stations']["Station"]
    print("Dit zijn de codes en de types van de 4 stations:")
    for station in stations:
        print("{} - {}".format(station["Code"],station["Type"]))
    print("\nDit zijn de synoniemen")
    for station in stations:
        if station["Synoniemen"] != None:
            for i in station["Synoniemen"]["Synoniem"]:
                print(i)
    print("\nDit is de lange naam van elk station")
    for station in stations:
            print("{:5}- {}".format(station["Code"],station["Namen"]["Lang"]))