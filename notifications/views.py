# Пример отправки уведомления конкретному пользователю
from django.http import JsonResponse

def test_notification(request):
    return JsonResponse({"message": "Уведомление работает!"})