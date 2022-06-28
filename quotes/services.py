from .models import Quote

def register_new_quote(ticker_info):
    try:
        quote = Quote.objects.get(ticker=ticker_info.get('ticker'), moment=ticker_info.get('moment'))
    except Quote.DoesNotExist:
        quote = None

    if not quote:
        quote = Quote.objects.create(ticker=ticker_info.get('ticker'), moment=ticker_info.get('moment'), value=ticker_info.get('value'))


def get_quotes_by_ticker(ticker):
    quotes = Quote.objects.filter(ticker=ticker)

    return quotes