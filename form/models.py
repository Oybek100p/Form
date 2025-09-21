from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.price} {self.author}"

# Create your models here.
