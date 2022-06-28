from django import forms
from .models import Tunnel

class TunnelForm(forms.ModelForm):

    class Meta():
        model = Tunnel
        fields = '__all__'