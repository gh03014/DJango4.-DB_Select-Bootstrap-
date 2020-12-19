from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board', views.board, name="board"),
]