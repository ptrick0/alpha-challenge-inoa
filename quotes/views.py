from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from tickers.models import Ticker
from .services import get_quotes_by_ticker_and_frequency
import json

@login_required
def index(request):
    tickers = Ticker.objects.all()
    serializedTickers = json.dumps([ticker.serialize() for ticker in tickers])

    return render(request, "quotes/list.html", context = {'tickers': tickers, 'serializedTickers': serializedTickers})

@login_required
def by_ticker_and_frequency(request):

    if(request.method == "POST"):
        tickerId = int(request.POST['tickerId'])
        frequency = request.POST['frequency']

        if not frequency or int(frequency) <= 0:
            frequency = 1
        else:
            frequency = int(frequency)

        ticker = get_object_or_404(Ticker, pk=tickerId)
        
        if ticker:
            quotes = get_quotes_by_ticker_and_frequency(tickerId, frequency)
            if quotes:
                return HttpResponse(json.dumps([quote.serialize() for quote in quotes]))

    return HttpResponse()