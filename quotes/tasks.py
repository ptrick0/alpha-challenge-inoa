import yfinance as yf
from tickers.models import Ticker
from .services import register_new_quote

def get_quotes():
    tickers = Ticker.objects.all()

    for ticker in tickers:
        tick = yf.Ticker(ticker.symbol+".SA")
        ticker_ok = False

        try:
            if (tick.info['regularMarketPrice']):
                ticker_ok = True
            else:
                tick = yf.Ticker(ticker.symbol)
                if (tick.info['regularMarketPrice']):
                    ticker_ok = True


            if ticker_ok:
                history = tick.history(period="2d", interval="1m")
                
                last_quote = history['Close'].iloc[-1]

                hist = history.iloc[-1] # Picking only last ticker update
                tick_dict = {
                    'ticker': ticker,
                    'moment': hist.name.tz_localize(None),
                    'value': hist["Close"]
                }
                register_new_quote(tick_dict)
        except:
            continue