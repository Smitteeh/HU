ticker_symbols = {
    'YAHOO':'YHOO',
    'GOOGLE INC':'GOOG',
    'Harley-Davidson':'HOG',
    'Yamana Gold':'AUY',
    'Sotheby’s':'BID',
    'inBev':'BUD'
}

def ticker(filename):
    ticket = ticker_symbols[filename]
    return ticket
def tickers(filename):
    ticket = ticker_symbols.get(filename)
    return ticket
Bedrijfsnaam = input('Enter company name: ')
Tickersymbol = input('Enter tickersymbol: ')

print(ticker(Bedrijfsnaam))
print(tickers(Tickersymbol))