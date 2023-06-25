from django.urls import path
from . import views

urlpatterns = [
    path('info', views.meet_the_team, name='meet_the_team'),
]
