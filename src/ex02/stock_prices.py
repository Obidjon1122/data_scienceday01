import sys

COMPANIES = {
'Apple': 'AAPL',
'Microsoft': 'MSFT',
'Netflix': 'NFLX',
'Tesla': 'TSLA',
'Nokia': 'NOK'
}

STOCKS = {
'AAPL': 287.73,
'MSFT': 173.79,
'NFLX': 416.90,
'TSLA': 724.88,
'NOK': 3.37
}

def stock_prices():
    if len(sys.argv)==2 and sys.argv[1].capitalize() not in COMPANIES:
        print("Unknown company")
    elif len(sys.argv)==2:
        print(STOCKS[COMPANIES[sys.argv[1].capitalize()]])

if __name__=='__main__':
    stock_prices()