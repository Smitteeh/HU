def standaardtarief(afstandKM):
    if afstandKM <= 50 and afstandKM > 0:
        res = afstandKM * 0.8
        return res
    elif afstandKM > 50:
        res = 15 + (afstandKM * 0.6)
        return res
    elif afstandKM <= 0:
        res = afstandKM * 0
        return res

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 and weekendrit == True:
        res = standaardtarief(afstandKM) * 0.7
    elif leeftijd >= 12 and leeftijd < 65 and weekendrit == True:
        res = standaardtarief(afstandKM)
    elif leeftijd >= 65 and weekendrit == True:
        res = standaardtarief(afstandKM) * 0.7
    elif leeftijd < 12 and weekendrit == False:
        res = standaardtarief(afstandKM) * 0.65
    elif leeftijd >= 12 and leeftijd < 65 and weekendrit == False:
        res = standaardtarief(afstandKM) * 0.6
    elif leeftijd >= 65 and weekendrit == False:
        res = standaardtarief(afstandKM) * 0.65
    return res

print((ritprijs(12, True, 45)))
