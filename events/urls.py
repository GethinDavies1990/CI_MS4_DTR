from django.urls import path
from . import views

urlpatterns = [
    path('book_event', views.book_event, name='book_event'),
    path('event_booked', views.event_booked, name='event_booked'),
]