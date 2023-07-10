from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    class Meta:
        app_label = 'book'
    # Add more fields as needed
    
    def __str__(self):
        return self.title

# Create your models here.
