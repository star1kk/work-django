from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=50, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('edit_user', args=[str(self.pk)])


