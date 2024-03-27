from django.db import models
from django.contrib.auth.models import User
from Books.models import Book

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    


    def __str__(self):
        return f"{self.quantity} x {self.book.title} for {self.user.username}"
