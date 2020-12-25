from django.db import models


class UserGroup(models.Model):
    name = models.CharField(max_length=200)
