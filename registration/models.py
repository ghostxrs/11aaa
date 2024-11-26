from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Custom_user_model(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)