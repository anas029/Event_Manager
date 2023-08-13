from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username','phone_number','gender']

    def __str__(self):
        return self.username