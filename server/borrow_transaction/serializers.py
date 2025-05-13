from rest_framework import serializers

from .models import BorrowTransaction, Book, User

from book.serializers import BookSerializer
from user.serializers import UserSerializer


class BorrowAndReturnSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        error_messages={"does_not_exist": "Book not found."},
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={"does_not_exist": "User not found."},
    )
    status = serializers.ChoiceField(
        choices=BorrowTransaction.STATUS_CHOICES,
        error_messages={
            "invalid_choice": "The status you provided is not valid. Choose from: borrowed, returned."
        },
    )

    class Meta:
        model = BorrowTransaction
        fields = ["book", "user", "status", "date"]


class BorrowTransactionSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = BorrowTransaction
        fields = ["id", "book", "book_id", "user", "user_id", "status", "date"]
        read_only_fields = ["book", "user"]
