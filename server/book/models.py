from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available_copies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["isbn"], name="unique_isbn")]
        ordering = ["-created_at"]

    def borrow_copy(self):
        if self.available_copies == 0:
            raise ValueError("No copies left.")

        self.available_copies -= 1
        self.save()
