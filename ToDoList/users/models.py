from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, null=False)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)