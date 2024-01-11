from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField()
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return self.username

