from django.db import models


class Program(models.Model):
    TYPE = (
        ("M", "Movie"),
        ("S", "Series"),
    )

    title = models.CharField(max_length=50)
    type = models.CharField(
        max_length=1, choices=TYPE, blank=False, null=False, default="M"
    )
    release_date = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
