from django.urls import path

from . import views

urlpatterns = [
    path('team/', views.TeamView.as_view(), name='team'),
    path('team/<int:pk>/', views.TeamView.as_view(), name='team'),
    path('player/', views.PlayerView.as_view(), name='player'),
    path('player/<int:pk>/', views.PlayerView.as_view(), name='player'),
]