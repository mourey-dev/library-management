from django.urls import include, path

from borrow_transaction.views import borrow_book, return_book, get_transactions

urlpatterns = [
    path("api/books/", include("book.urls", namespace="books_api")),
    path("api/users/", include("user.urls", namespace="users_api")),
    path("api/transactions/", get_transactions, name="transactions_api"),
    path("api/borrow/", borrow_book, name="borrow_book_api"),
    path("api/return/<int:borrow_id>/", return_book, name="return_book_api"),
]
