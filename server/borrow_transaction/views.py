from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import (
    BorrowTransaction,
    BorrowAndReturnSerializer,
    BorrowTransactionSerializer,
)


@api_view(["GET"])
def get_transactions(request):
    borrow_transactions = BorrowTransaction.objects.all()
    borrow_transactions_serializer = BorrowTransactionSerializer(
        borrow_transactions, many=True
    )

    # Return a response with both the book details and the associated borrow transactions
    return Response(
        {
            "borrow_transactions": borrow_transactions_serializer.data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def borrow_book(request):
    serializer = BorrowAndReturnSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    book = serializer.validated_data["book"]

    try:
        book.borrow_copy()
        serializer.save()

        return Response(
            {
                "message": "Book borrowed successfully.",
            },
            status=status.HTTP_201_CREATED,
        )

    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def return_book(request, borrow_id):
    # Get the BorrowTransaction by ID
    transaction = get_object_or_404(BorrowTransaction, pk=borrow_id)

    # Check if the transaction has already been returned
    if transaction.status == "returned":
        return Response(
            {"error": "This book has already been returned."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update the status and the return date
    transaction.status = "returned"
    transaction.date = request.data.get(
        "date", None
    )  # Update the return date if provided
    transaction.save()

    # Update the book's available copies
    book = transaction.book
    book.available_copies += 1
    book.save()

    return Response(
        {"message": "Book returned successfully."},
        status=status.HTTP_200_OK,
    )
