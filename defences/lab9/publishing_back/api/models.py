from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField()
    description = models.TextField()  
    city = models.CharField()
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField()
    synopsis = models.TextField()  
    price = models.FloatField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    