de_lijst = eval(input("Geef een lijst met minimaal 10 strings"))
uitkomst = []
for lang in de_lijst:
    if len(lang) == 4:
        uitkomst.append(lang)

print(uitkomst)
