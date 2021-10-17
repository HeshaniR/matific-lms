from django.urls import path

from . import views

urlpatterns = [
    path('players', views.get_players, name='get_players'),
    path('players/<int:filter>/', views.get_filtered_players, name='get_filtered_players'),
    path('player/<int:player_id>/', views.get_player_details, name='get_player_details'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('create', views.create, name='create'),
    path('stats', views.get_user_stats, name='get_user_stats')

]
