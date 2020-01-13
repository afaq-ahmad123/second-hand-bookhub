from django.db import models
from phone_field import PhoneField

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=99)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=99, unique=True)
    password = models.CharField(max_length=99)
    contact = models.CharField(max_length=29)
    #PhoneField(blank=True, help_text='Contact phone number',E164_only=False)
    address = models.CharField(max_length=99)
