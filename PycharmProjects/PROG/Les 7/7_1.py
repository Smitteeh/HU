som = []
while True:
    Getal = eval(input('Geef een getal'))
    if Getal == 0:
        print ('Er zijn ' + str(len(som)) + ' getallen ingevoerd, de som is ' + str(sum(som)))
        break
    else:
        som.append(Getal)
