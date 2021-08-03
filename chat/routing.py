from django.urls import re_path
from . import consumers

# relative path for advance path which the regular path string fails to meet our reuired path

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
]