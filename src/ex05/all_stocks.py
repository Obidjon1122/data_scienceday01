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
def all_stocks():
    if len(sys.argv)==2:
        tickers=[]
        tickers1=sys.argv[1].split(',')
        for k in tickers1:
            tickers.append(k.strip())
        t=True
        for it in tickers:
            if len(it)==0:
                t=False
        if t:
            for item in tickers:
                if item.upper() in STOCKS:
                    for com in COMPANIES:
                        if COMPANIES[com]==item.upper():
                            print(item.upper() +" is a ticker symbol for "+com)
                            break
                elif item.capitalize() in COMPANIES:
                    print(item.capitalize()+" stock price is "+str(STOCKS[COMPANIES[item.capitalize()]]))
                else:
                    print(item+" is an unknown company or an unknown ticker symbol")
if __name__=='__main__':
    all_stocks()