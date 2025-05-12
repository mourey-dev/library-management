from django.core.management.base import BaseCommand
from book.models import Book


class Command(BaseCommand):
    help = "Create 10 predefined books"

    def handle(self, *args, **kwargs):
        books = [
            {
                "isbn": "9780140449136",
                "title": "The Odyssey",
                "author": "Homer",
                "available_copies": 10,
            },
            {
                "isbn": "9780439139601",
                "title": "Harry Potter and the Goblet of Fire",
                "author": "J.K. Rowling",
                "available_copies": 15,
            },
            {
                "isbn": "9780061120084",
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "available_copies": 12,
            },
            {
                "isbn": "9780553213119",
                "title": "Dracula",
                "author": "Bram Stoker",
                "available_copies": 8,
            },
            {
                "isbn": "9781501173219",
                "title": "It Ends With Us",
                "author": "Colleen Hoover",
                "available_copies": 20,
            },
            {
                "isbn": "9780451524935",
                "title": "1984",
                "author": "George Orwell",
                "available_copies": 14,
            },
            {
                "isbn": "9780141439600",
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "available_copies": 9,
            },
            {
                "isbn": "9780544003415",
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "available_copies": 13,
            },
            {
                "isbn": "9780141182803",
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "available_copies": 11,
            },
            {
                "isbn": "9780385472579",
                "title": "Zen and the Art of Motorcycle Maintenance",
                "author": "Robert M. Pirsig",
                "available_copies": 10,
            },
        ]

        for book in books:
            Book.objects.create(**book)

        self.stdout.write(self.style.SUCCESS("Successfully created 10 book entries."))
