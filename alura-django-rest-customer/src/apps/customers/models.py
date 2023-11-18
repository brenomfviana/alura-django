from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    cellphone = models.CharField(max_length=14)
    active = models.BooleanField()

    def __str__(self):
        return self.name
