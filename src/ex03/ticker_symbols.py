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

def ticker_symbols():
    res=[]
    if len(sys.argv)==2 and sys.argv[1].upper() in STOCKS:
      for comp_name in COMPANIES:
          if COMPANIES[comp_name]==sys.argv[1].upper():
              print(comp_name,STOCKS[COMPANIES[comp_name]])
              break
    elif len(sys.argv)==2:
        print("Unknown ticker")

if __name__=='__main__':
    ticker_symbols()