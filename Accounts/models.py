from django.db import models


class Login(models.Model):
    def __str__(self):
        return self.email

    email = models.CharField(max_length=25)


class Register(models.Model):
    
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class Product(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
