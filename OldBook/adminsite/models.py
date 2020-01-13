from django.db import models

# Create your models here.
class adminUser(models.Model):
    name = models.CharField(max_length=48)
    email = models.CharField(max_length=98)
    password = models.CharField(max_length=98)
    id = models.ForeignKey('login.user', on_delete=models.CASCADE, primary_key=True)
