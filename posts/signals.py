from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Post

@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notifications_{instance.author.id}",
            {
                "type": "send.notification",
                "message": f"Новый пост: {instance.title}",
                "data": {
                    "post_id": instance.id,
                    "author": instance.author.username
                }
            }
        )