from hashlib import md5

from django.contrib.auth.models import AbstractUser
from django.db import models

from .facility import Facility


class User(AbstractUser):
    facilities = models.ManyToManyField(Facility)

    @property
    def gravatar_hash(self):
        if self.email is not None and self.email != '':
            hashed = md5(str(self.email).strip().lower().encode('utf-8')).hexdigest()
            return hashed

        hashed = md5(str(self.get_full_name()).strip().lower().encode('utf-8')).hexdigest()
        return hashed

    @property
    def avatar_url(self):
        return f"https://www.gravatar.com/avatar/{self.gravatar_hash}?d=monsterid"
