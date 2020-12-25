from django.db import models
from .facility import Facility


class StashLocation(models.Model):
    name = models.CharField(max_length=200)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
