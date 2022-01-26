from django.db import models


class Points(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    DeBe = models.FloatField()
