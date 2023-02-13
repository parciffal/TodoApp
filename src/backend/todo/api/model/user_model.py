from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.username
