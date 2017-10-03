def monopolyworp():
    import random
    Beurten = 0
    while True:
        Dobbelsteen1 = random.randrange(1,3)
        Dobbelsteen2 = random.randrange(1,3)
        Samen = str(Dobbelsteen1) + ' + ' + str(Dobbelsteen2) + ' = ' + str(Dobbelsteen1+Dobbelsteen2) + ' '
        if Beurten == 2:
            Samen = str (Dobbelsteen1) + ' + ' + str (Dobbelsteen2) + ' = ' + str (Dobbelsteen1 + Dobbelsteen2) + ' (Gevangenis)'
            print(Samen)
            break
        elif Dobbelsteen1 == Dobbelsteen2:
            Samen = str(Dobbelsteen1) + ' + ' + str(Dobbelsteen2) + ' = ' + str(Dobbelsteen1+Dobbelsteen2) + ' (Dubbel)'
            True
            print(Samen)
            Beurten = Beurten + 1
        else:
            print (Samen)
            break

monopolyworp()