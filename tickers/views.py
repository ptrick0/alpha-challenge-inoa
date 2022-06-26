from django.shortcuts import render, redirect, HttpResponse
from .models import Ticker
from .forms import TickerForm
from .services import get_ticker_info
import json

# Create your views here.
def index(request):
    tickers = Ticker.objects.all()
    return render(request, "tickers/list.html", context={'tickers': tickers})

def new(request):

    if request.method == 'POST':
        form = TickerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('list_tickers')
    else:
        form = TickerForm()

    return render(request, "tickers/new.html", context={'form': form})

def ticker_info(request):
    if(request.method == "POST"):
        if request.POST['ticker']:
            ticker = request.POST['ticker']

            data = get_ticker_info(ticker)

            if data['status'] == 200:
                return HttpResponse(json.dumps(data['info']))
            else:
                return HttpResponse(status=data['status'])
        else:
            return HttpResponse(status=500)