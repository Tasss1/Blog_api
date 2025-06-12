from django.contrib import admin
from .models import Notification
# Изменяем импорт на относительный
from .services import send_notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Только при создании нового уведомления
            send_notification(
                user=obj.user,
                message=obj.message,
                data={"admin_id": request.user.id}
            )