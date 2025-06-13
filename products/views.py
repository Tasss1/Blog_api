from rest_framework import viewsets, permissions
from .models import Product, UserProfile
from .serializers import ProductSerializer, UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema  # 👈 добавлено

@extend_schema(tags=['Products'])  # 👈 Название для Swagger
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        product = self.get_object()
        product.buyers.add(request.user)
        return Response({'status': 'product bought'})


@extend_schema(tags=['Profiles'])  # 👈 Название для Swagger
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
