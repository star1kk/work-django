from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    article = models.TextField(default=None)

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])

    def __str__(self):
        return self.title
