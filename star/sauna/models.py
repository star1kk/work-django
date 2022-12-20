from django.db import models
from django.urls import reverse


class Sauna(models.Model):
    photo1 = models.URLField(max_length=200, default=None)
    photo2 = models.URLField(max_length=200, default=None)
    photo3 = models.URLField(max_length=200, default=None)
    description = models.TextField(default=None)
    price = models.PositiveIntegerField(default='')
    full_description = models.TextField(default=None)

    def get_absolute_url(self):
        return reverse('sauna_detail', args=[str(self.id)])

    def __str__(self):
        return str(self.description)
