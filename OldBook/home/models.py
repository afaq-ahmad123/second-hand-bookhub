from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=99)
    id = models.IntegerField(primary_key=True, auto_created=True)
    price = models.IntegerField(primary_key=False)
    writer = models.CharField(max_length=49)
    image = models.CharField(max_length=149, default="/media/images/home/default_book.jpg")
    sellerID = models.ForeignKey('login.user', on_delete=models.CASCADE)


class bids(models.Model):
    class Meta:
        unique_together = (('bookID', 'buyerID'),)

    bookID = models.ForeignKey(book, on_delete=models.CASCADE)
    buyerID = models.ForeignKey('login.user', on_delete=models.CASCADE)


class exchange(models.Model):
    class Meta:
        unique_together = (('sellerBookID', 'buyerBookID', 'sellerID', 'buyerID'),)

    sellerBookID = models.ForeignKey(book, on_delete=models.CASCADE, related_name='sellerBook')
    buyerBookID = models.ForeignKey(book, on_delete=models.CASCADE, related_name='buyerBook')
    sellerID = models.ForeignKey('login.user', on_delete=models.CASCADE, related_name='seller')
    buyerID = models.ForeignKey('login.user', on_delete=models.CASCADE, related_name='buyer')


class giveAway(models.Model):
    class Meta:
        unique_together = (('bookID', 'sellerID', 'buyerID'),)
    bookID = models.ForeignKey(book, on_delete=models.CASCADE)
    sellerID = models.ForeignKey('login.user', on_delete=models.CASCADE, related_name='sellers')
    buyerID = models.ForeignKey('login.user', on_delete=models.CASCADE, related_name='buyers')
