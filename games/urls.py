from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/<str:player_name>/', views.player_games, name='player_games'),
]
