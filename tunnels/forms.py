from django import forms
from .models import Tunnel
from tickers.models import Ticker

class TunnelForm(forms.ModelForm):

    class Meta():
        model = Tunnel
        fields = ['ticker', 'topLimit', 'bottomLimit', 'frequency']
        widgets = {
            'ticker': forms.Select(attrs={'class': ''}, choices=Ticker.objects.all()),
            'topLimit': forms.NumberInput(attrs={'class': 'input'}),
            'bottomLimit': forms.NumberInput(attrs={'class': 'input'}),
            'frequency': forms.NumberInput(attrs={'class': 'input'}),
        }
