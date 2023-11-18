from django.db import models

from .trip_class import TripClass


class Ticket(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_day = models.DateField()
    return_day = models.DateField()
    query_date = models.DateField()
    trip_class = models.CharField(max_length=4, choices=TripClass.choices, default=0)
    extra_info = models.TextField(max_length=200, blank=True)
