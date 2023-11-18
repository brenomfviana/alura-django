from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=20)
    predator = models.BooleanField(default=False)
    poisonous = models.BooleanField(default=False)
    domestic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
