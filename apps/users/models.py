from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    REQUIRED_FIELDS = ["email"]
    # USERNAME_FIELD = "email"

    # email = models.EmailField(unique = True)

    def save(self, *args,**kwargs) -> None:
        self.username = self.email.split('@')[0]
        return super().save(*args,**kwargs)
