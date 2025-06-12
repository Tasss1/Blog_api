# products/admin.py
from django.contrib import admin
from .models import Product, UserProfile

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'created_at')
    list_filter = ('seller', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('buyers',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'phone')
    readonly_fields = ('user',)