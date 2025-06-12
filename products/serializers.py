# products/serializers.py
from rest_framework import serializers
from .models import Product, UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    buyers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'seller', 'buyers', 'created_at', 'updated_at']
        read_only_fields = ['seller']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'phone', 'address']