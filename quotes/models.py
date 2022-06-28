from datetime import datetime
from django.db import models

class Quote(models.Model):
    ticker = models.ForeignKey('tickers.Ticker', on_delete=models.CASCADE)
    moment = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return self.ticker.symbol + ' - ' + self.moment.strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(self.value)

    def serialize(self):
        return {
            'moment': self.moment.strftime("%Y-%m-%d %H:%M:%S"),
            'value': self.value
        }