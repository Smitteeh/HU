def seizoen(maand):
    if maand >=3 and maand <= 5:
        print('Lente')
    if maand >=6 and maand <= 8:
        print('Zomer')
    if maand >=9 and maand <= 11:
        print('Herfst')
    if maand > 0 and maand <= 2 or maand >=12 and maand <13:
        print('Winter')

