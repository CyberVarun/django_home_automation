from django.db import models

# Create your models here.
# model to store username as email and password

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email