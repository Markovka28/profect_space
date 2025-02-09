from django.db import models

class AstronomicalObject(models.Model):
    name = models.CharField(max_length=200)
    object_type = models.CharField(max_length=100)
    ra = models.FloatField()  # Прямое восхождение
    dec = models.FloatField() # Склонение
    magnitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
