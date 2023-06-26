from django.urls import path
from . import views

urlpatterns = [
    path('book_event', views.book_event, name='book_event'),
    path('event_booked', views.event_booked, name='event_booked'),
    path('user_panel', views.user_panel, name='user_panel'),
    path('user_update_event/<int:id>', views.user_update_event, name='user_update_event'),
    path('user_update_event_submit/<int:id>', views.user_update_event_submit, name='user_update_event_submit(request, id)'),
    path('staff-panel', views.staff_panel, name='staff_panel'),
]