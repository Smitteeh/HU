def standaardtarief(afstandKM):
    #berekend hoeveel je voor x aantal kilometers betaald.
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
    #geeft de prijs van een rit bij bepaalde leeftijd en afstand en of het weekend is.
   if leeftijd < 12 or leeftijd >= 65:
       if weekendrit == True:
           res = standaardtarief(afstandKM) * 0.65
       else:
           res = standaardtarief(afstandKM) * 0.7
   else:
       if weekendrit == True:
           res = standaardtarief (afstandKM) * 0.6
       else:
           res = standaardtarief (afstandKM)
   return res
print((ritprijs(65, True, 51)))