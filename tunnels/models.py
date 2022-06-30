from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from tickers.models import Ticker
from django.contrib.auth.models import User

class Tunnel(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topLimit = models.FloatField( validators=[MinValueValidator(0.0)] )
    bottomLimit = models.FloatField( validators=[MinValueValidator(0.0)])
    frequency = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(59)])
    emailNotify = models.BooleanField()

    def __str__(self):
        return self.user.username + " - " + self.ticker.symbol

    def serialize(self):
        return {
            'id': self.pk,
            'ticker': self.ticker.serializeByFrequency(self.frequency),
            'topLimit': self.topLimit,
            'bottomLimit': self.bottomLimit,
            'frequency': self.frequency,
            'emailNotify': self.emailNotify
        }