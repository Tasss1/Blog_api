from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Принимаем соединение без проверок (для теста)
        await self.send(text_data="✅ WebSocket подключен!")

    async def disconnect(self, close_code):
        pass