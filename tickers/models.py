from django.db import models
from quotes.services import get_quotes_by_ticker

class Ticker(models.Model):
    symbol = models.CharField(unique=True, max_length=6)
    name = models.TextField()
    imageUrl = models.TextField()

    def __str__(self):
        return self.symbol + ' - ' + self.name

    def serialize(self):
        quotes = get_quotes_by_ticker(self)
        return {
            'symbol': self.symbol,
            'name': self.name,
            'imageUrl': self.imageUrl,
            'quotes': [quote.serialize() for quote in quotes]
        }