from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    how_to_cook = models.TextField()  # Modo de preparo
    time = models.IntegerField()  # Tempo de preparo
    recipe_yield = models.CharField(max_length=100)  # Rende para quantas pessoas?
    category = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
