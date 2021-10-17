from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:team_id>/', views.get_team_details, name='get_team_details'),
]