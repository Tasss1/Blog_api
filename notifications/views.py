from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema  # 👈 добавлено

@extend_schema(tags=['Notifications'])  # 👈 Название для Swagger
@api_view(['GET'])
def test_notification(request):
    return JsonResponse({"message": "Уведомление работает!"})
