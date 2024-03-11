from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
