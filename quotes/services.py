from .models import Quote
from django.db.models import F

def register_new_quote(ticker_info):
    try:
        quote = Quote.objects.get(ticker=ticker_info.get('ticker'), moment__startswith=ticker_info.get('moment').strftime("%Y-%m-%d %H:%M"))
    except Quote.DoesNotExist:
        quote = None

    if not quote:
        quote = Quote.objects.create(ticker=ticker_info.get('ticker'), moment=ticker_info.get('moment'), value=ticker_info.get('value'))


def get_quotes_by_ticker(ticker):
    quotes = Quote.objects.filter(ticker=ticker)

    return quotes

def get_quotes_by_ticker_and_frequency(ticker, frequency=1):
    quotes = Quote.objects.annotate(minute_mod = (F('moment__minute') % frequency)).filter(ticker=ticker, minute_mod=0)

    return quotes