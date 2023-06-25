from django.urls import path
from . import views

urlpatterns = [
    path('meet_the_team', views.meet_the_team, name='meet_the_team'),
    path('how_we_started', views.how_we_started, name='how_we_started'),
]
