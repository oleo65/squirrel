from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=200)
