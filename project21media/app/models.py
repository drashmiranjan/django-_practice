from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.IntegerField()
    address = models.TextField()
    photo = models.ImageField()
    
    def __str__(self):
        self.username.username