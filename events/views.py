from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Events
from profiles.models import UserProfile
from django.contrib import messages


def book_event(request):
    """
    Book event function,
    """
    weekdays = validWeekday(60)
    validateWeekdays =isWeekdayValid(weekdays)

    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        day = reques.POST.get('day')
        if event_type == None:
            messages.warning(request, "Please select an event type!")



