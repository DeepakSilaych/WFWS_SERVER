from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    waterlevel = models.FloatField()
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
