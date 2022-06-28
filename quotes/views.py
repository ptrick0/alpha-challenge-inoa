from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tickers.models import Ticker
import json

@login_required
def index(request):
    tickers = Ticker.objects.all()
    serializedTickers = json.dumps([ticker.serialize() for ticker in tickers])

    return render(request, "quotes/list.html", context = {'tickers': tickers, 'serializedTickers': serializedTickers})
    