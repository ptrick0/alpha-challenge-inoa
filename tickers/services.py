import yfinance as yf

def get_ticker_info(ticker):
    tick = yf.Ticker(ticker+".SA")

    if (tick.info['regularMarketPrice']):
        return {'status': 200, 'info': tick.info}
    else:
        tick = yf.Ticker(ticker)
        if (tick.info['regularMarketPrice']):
            return {'status': 200, 'info': tick.info}
            
    return {'status': 404, 'info': {}}