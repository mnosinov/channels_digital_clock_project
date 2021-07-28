from django.urls import path
from .consumers import ws_consumer

# path to call the consumer
ws_urlpatterns = [
    path('msg/', ws_consumer.as_asgi()),
]
