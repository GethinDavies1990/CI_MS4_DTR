from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Events
from profiles.models import UserProfile
from django.contrib import messages


def book_event(request):
    """
    Book event function,
    """
    weekdays = valid_weekday(60)
    validate_weekdays =is_weekday_valid(weekdays)

    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        day = request.POST.get('day')
        if event_type == None:
            messages.warning(request, "Please select an event type!")
            return redirect('book_event')

        request.session['day'] = day
        request.session['event_type'] = event_type

        return redirect('event_booked')

    return render(request, 'book_event.html', {
        'weekdays':weekdays,
        'validate_weekdays': validate_weekdays,
    })


def event_booked(request):
    user = request.user
    times = [
        '2PM', '5.30PM'
    ]
    today = datetime.now()
    min_date = today.strftime('%d-%m-%Y')
    max_date = strdeltatime

    day = request.session.get('day')
    event_type = request.session.get('event_type')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get('time')
        date = day_to_weekday(day)

        if event_type != None:
            if day <= max_date and day >= min_date:
                if date =='Thursday' or date == 'Friday' or date =='Saturday' or date == 'Sunday':
                    if Events.objects.filter(day=day).count() < 11:
                        if Events.objects.filter(day=day, time=time).count() < 1:
                            EventsForm = Events.objects.get_or_create(
                                user = user,
                                event_type = event_type,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Event Booked")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A event_type!")

    return render(request, 'event_booked.html', {
        'times':hour,
    })


def user_panel(request):
    user = request.user
    events = Events.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'user_panel.html', {
        'user':user,
        'events':events,
    })


def user_update_event(request, id):
    event = Events.objects.get(pk=id)
    user_date_selected = event.day
    today = datetime.today()
    min_date = today.strftime('%d-%m-%Y')

    delta24 = (user_date_selected).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = valid_weekday(22)

    #Only show the days that are not full:
    validate_weekdays = is_weekday_valid(weekdays)


    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['event_type'] = event_type

        return redirect('user_update_event_submit', id=id)


    return render(request, 'user_update_event.html', {
            'weekdays':weekdays,
            'validate_weekdays':validate_weekdays,
            'delta24': delta24,
            'id': id,
        })


def user_update_event_submit(request, id):
    user = request.user
    times = [
        "3 PM", "5:30 PM"
    ]
    today = datetime.now()
    min_date = today.strftime('%d-%m-%Y')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%d-%m-%Y')
    max_date = strdeltatime

    day = request.session.get('day')
    event_type = request.session.get('event_type')

    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = check_edit_times(times, day, id)
    event = Event.objects.get(pk=id)
    user_selected_time = Event.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = day_to_weekday(day)

        if event_type != None:
            if day <= max_date and day >= min_date:
                if date =='Thursday' or date == 'Friday' or date =='Saturday' or date == 'Sunday':
                    if Event.objects.filter(day=day).count() < 11:
                        if Event.objects.filter(day=day, time=time).count() < 1 or user_selected_time == time:
                            EventForm = Event.objects.filter(pk=id).update(
                                user = user,
                                event_type = event_type,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "event Edited!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A event_type!")
        return redirect('user_panel')


    return render(request, 'user_update_event_submit.html', {
        'times':hour,
        'id': id,
    })



