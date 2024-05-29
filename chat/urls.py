from django.urls import path
from .views import *


urlpatterns = [
    path ("", index, name='index'),
    path("chat/<str:room_name>/", room, name="room"),
]
