# products/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = router.urls