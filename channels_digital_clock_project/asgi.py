import os

# import get_asgi_application to handle http protocol
from django.core.asgi import get_asgi_application

# import ProtocolTypeRouter and URLRouter to set the websocket routing
from channels.routing import ProtocolTypeRouter, URLRouter

# import AuthMiddlewareStack to handle websocket
from channels.auth import AuthMiddlewareStack

# import websocket routing
from socketapp.routing import ws_urlpatterns

# assign value for DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_digital_clock_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
