from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # takes main page
    path('<str:room_name>/', views.room, name='room'),  # takes to the chat room
]

'''
string will be the room_name variable which will take us to desired data through room name in the view
'''
