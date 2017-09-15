Afstand = eval(input("Hoeveel kilometer reist u?"))

if Afstand <= 50:
    def standaardtarief(afstandKM):
        res = afstandKM * 0.8
        return res
elif Afstand > 50:
    def standaardtarief(afstandKM):
        res = 15 + (afstandKM * 0.6)
        return res

print(standaardtarief(Afstand))

