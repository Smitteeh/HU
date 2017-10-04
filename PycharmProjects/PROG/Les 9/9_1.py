bedrag = 4356
while True:
    try:
        aantal = input ('Vul hier in hoeveel mensen mee gaan: ')
        if aantal >= 0:
            kosten = bedrag / int(aantal)
            print('Als er ' + str(aantal) + ' mensen mee gaan kost dat ' + str(int(kosten)) + ' Euro')
    except ValueError:
        print('Je moet een cijfer invullen.')
    except ZeroDivisionError:
        print('Zonder personen kan er geen bedrag berekent worden')
    except TypeError:
        print('De getallen moeten positief zijn')
    except:
        print('Er is een onbekende fout opgetreden!')
