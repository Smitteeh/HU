Leeftijd = eval(input('Wat is uw leeftijd?'))
Paspoort  = input('Heeft u een Nederlands paspoort?')

if Paspoort == 'ja' and Leeftijd > 18:
    print('Gefeliciteerd, u mag stemmen!')
else:
    print('Helaas, u mag niet stemmen.')
