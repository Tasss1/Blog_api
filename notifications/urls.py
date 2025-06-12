from django.urls import path
from .views import test_notification

urlpatterns = [
    path('test-notify/', test_notification),
]