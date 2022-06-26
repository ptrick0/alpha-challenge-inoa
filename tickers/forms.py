from django import forms
from .models import Ticker

class TickerForm(forms.ModelForm):

    class Meta():
        model = Ticker
        fields = ['symbol', 'name', 'imageUrl']
        widgets = {
            'symbol': forms.TextInput(attrs={'class': 'input'}),
            'name': forms.TextInput(attrs={'class': 'input', 'readonly': True}),
            'imageUrl': forms.TextInput(attrs={'class': 'input', 'readonly': True}),
        }