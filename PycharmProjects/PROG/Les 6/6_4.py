studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    lijst = []
    for gemiddelde in studentencijfers:
        gemiddeld = sum(gemiddelde) / len(gemiddelde)
        lijst.append(gemiddeld)
    return lijst

def gemiddelde_van_alle_studenten(studentencijfers):
    alles = gemiddelde_per_student(studentencijfers)
    antwoord = sum(alles) / len(alles)

    return antwoord

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))