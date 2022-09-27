from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=120)
    author_name= models.CharField(max_length=120)
    price=models.FloatField()
    quantity=models.IntegerField()
    publisher=models.CharField(max_length=120)

    def __str__(self):
        return self.book_name
