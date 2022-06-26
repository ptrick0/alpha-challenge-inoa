from django.db import models

class Ticker(models.Model):
    symbol = models.CharField(unique=True, max_length=6)
    name = models.TextField()
    imageUrl = models.TextField()

    def __str__(self):
        return self.symbol + ' - ' + self.name