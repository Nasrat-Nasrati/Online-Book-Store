from django.db import models
from django.contrib.auth.models import User
from Books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order by {self.user.username} for {self.quantity} x {self.book.title} on {self.order_date}"