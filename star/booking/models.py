from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    sauna = models.ForeignKey("sauna.Sauna", on_delete=models.PROTECT, null=True)
    entry_date = models.DateField(auto_now=False, auto_now_add=False)
    entry_time = models.TextField()
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    hours = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(24)])

    def get_absolute_url(self):
        return reverse('booking_detail', args=[str(self.pk)])