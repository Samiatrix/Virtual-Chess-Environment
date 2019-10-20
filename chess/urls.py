from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('play/',GamePlay.as_view(),name="play"),
]