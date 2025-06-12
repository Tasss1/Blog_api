from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from rest_framework.routers import DefaultRouter
from notifications.routing import websocket_urlpatterns

# Создаем главный router
main_router = DefaultRouter()

# Подключаем endpoints из приложений
from posts.views import PostViewSet, CommentViewSet
from products.views import ProductViewSet, UserProfileViewSet

main_router.register('posts', PostViewSet, basename='posts')
main_router.register('comments', CommentViewSet, basename='comments')
main_router.register('products', ProductViewSet, basename='products')
main_router.register('profiles', UserProfileViewSet, basename='profiles')

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Основные API endpoints
    path('api/', include(main_router.urls)),

    # Документация API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Уведомления
    path('notifications/', include('notifications.urls')),

    # WebSockets
    path('ws/', include(websocket_urlpatterns)),

    # Для тестирования WebSocket (опционально)
    path('test-notify/', include('notifications.urls')),
]