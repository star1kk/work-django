from django.db import models
import datetime

# Create your models here.


class Booking(models.Model):
    Date = models.DateTimeField(('Date'), default=datetime.datetime.now())
    suana = [
        (1,'hamam'),(2,'rus'),(3,'finsk')
    ]
    choiced_sauna = models.CharField(choices=suana)
