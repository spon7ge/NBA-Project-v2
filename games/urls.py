from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name='home'),
    path('players/<str:player_name>/', views.player_games, name='player_games'),
    path('blog/', views.blog, name='nba-blog'),
]
