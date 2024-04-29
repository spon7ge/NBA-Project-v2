from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='nba-home'),
    path('about/', views.about, name='nba-about'),
]