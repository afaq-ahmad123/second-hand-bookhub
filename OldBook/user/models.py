from django.db import models
from django.apps import apps

# Create your models here.



class cart(models.Model):
    id = models.ForeignKey('home.book', on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField(primary_key=False, null=True)


class featuredSellers(models.Model):
    id = models.ForeignKey('login.user', on_delete=models.CASCADE, primary_key=True)
    bookCount = models.IntegerField(primary_key=False)

