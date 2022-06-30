from django.db import models
from tickers.models import Ticker
from django.contrib.auth.models import User

class Tunnel(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topLimit = models.FloatField() # non negative
    bottomLimit = models.FloatField() # non negative
    frequency = models.IntegerField() # non negative > 0

    def __str__(self):
        return self.user.username + " - " + self.ticker.symbol

    def serialize(self):
        return {
            'id': self.pk,
            'ticker': self.ticker.serializeByFrequency(self.frequency),
            'topLimit': self.topLimit,
            'bottomLimit': self.bottomLimit,
            'frequency': self.frequency
        }