from django.db import models

from book.models import Book
from user.models import User


class BorrowTransaction(models.Model):
    STATUS_CHOICES = [("borrowed", "Borrowed"), ("returned", "Returned")]

    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, related_name="book_borrow_transaction"
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="user_borrow_transaction"
    )
    date = models.DateField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
