from django.db import models
from users.models import User
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    published_date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ['author', 'title']