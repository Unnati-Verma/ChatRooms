'''
Expecting the application here. Here, we're setting a router between consumers(views) and ASGI so that it can send the data.
Just like the urls.py files in the project and application.
'''

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# to find who the user is with authmiddlestack
# second import is just the mechanism for routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# because we want to use django authentication we are wrapping the urls in the authmiddlewarestack

# urlrouter is the route of url