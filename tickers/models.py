from django.db import models
from quotes.services import get_quotes_by_ticker, get_quotes_by_ticker_and_frequency

class Ticker(models.Model):
    symbol = models.CharField(unique=True, max_length=6)
    name = models.TextField()
    imageUrl = models.TextField()

    def __str__(self):
        return self.symbol + ' - ' + self.name

    def serialize(self):
        quotes = get_quotes_by_ticker(self).order_by('-id')[:15:-1] #last 15 inserted quotes
        
        return {
            'symbol': self.symbol,
            'name': self.name,
            'imageUrl': self.imageUrl,
            'quotes': [quote.serialize() for quote in quotes]
        }

    def serializeByFrequency(self, frequency):
        quotes = get_quotes_by_ticker_and_frequency(self, frequency).order_by('-id')[:15:-1] #last 15 inserted quotes by frequency in minutes
        
        return {
            'symbol': self.symbol,
            'name': self.name,
            'imageUrl': self.imageUrl,
            'quotes': [quote.serialize() for quote in quotes]
        }