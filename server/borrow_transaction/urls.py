from django.urls import path, include

from rest_framework import routers

from .views import BorrowTransactionViewSet

router = routers.DefaultRouter()
router.register(r"", BorrowTransactionViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "borrow_transaction"
