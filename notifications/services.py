from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(user, message, data=None):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notifications_{user.id}",
        {
            "type": "send.notification",
            "message": message,
            "data": data or {}
        }
    )