// static/js/notifications.js
const notificationSocket = new WebSocket(
    `ws://${window.location.host}/ws/notifications/`
);

notificationSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if (data.type === 'notification') {
        showNotification(data.message);
    }
};

function showNotification(message) {
    const notificationsDiv = document.getElementById('notifications');
    const notificationElement = document.createElement('div');
    notificationElement.className = 'alert alert-info';
    notificationElement.innerText = message;
    notificationsDiv.prepend(notificationElement);
    
    // Авто-скрытие через 5 секунд
    setTimeout(() => {
        notificationElement.remove();
    }, 5000);
}