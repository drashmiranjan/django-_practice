from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE means here if we delete a data from parent table then the data was deleted from child table
    pno = models.IntegerField()
    address = models.TextField() # here text_field is used to give a text area in frontend
    profile_pic = models.ImageField()
    
    def __str__(self):
        return self.username.username