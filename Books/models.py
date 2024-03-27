from django.db import models
from BookCategories.models import BookCategory

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_covers = models.ImageField(upload_to='book_covers/', null=True)
    isbn = models.CharField(max_length=13)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
