from django.core.management.base import BaseCommand
from user.models import User
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Create 10 predefined users"

    def handle(self, *args, **kwargs):
        users = [
            {"first_name": "Alice", "last_name": "Johnson"},
            {"first_name": "Bob", "last_name": "Smith"},
            {"first_name": "Charlie", "last_name": "Davis"},
            {"first_name": "Diana", "last_name": "Garcia"},
            {"first_name": "Ethan", "last_name": "Martinez"},
            {"first_name": "Fiona", "last_name": "Lee"},
            {"first_name": "George", "last_name": "Walker"},
            {"first_name": "Hannah", "last_name": "Nguyen"},
            {"first_name": "Isaac", "last_name": "Brown"},
            {"first_name": "Julia", "last_name": "Clark"},
        ]

        created_count = 0
        for user in users:
            try:
                User.objects.create(**user)
                created_count += 1
            except IntegrityError:
                self.stdout.write(
                    self.style.WARNING(
                        f"User '{user['first_name']} {user['last_name']}' already exists (skipped)."
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {created_count} users.")
        )
