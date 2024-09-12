from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password as make, check_password as check
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, null=False)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username

    def check_password(self, raw_password):
        return check(raw_password, self.password)