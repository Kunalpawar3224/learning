from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    descritory = models.CharField(max_length=200)
    active_field = models.BooleanField(default=True)

    def __str__(self):
        return self.name