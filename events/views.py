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
            return redirect('book_event')

        request.session['day'] = day
        request.session['event_type'] = event_type

        return redirect('eventBooked')

    return render(request, 'book_event.html', {
        'weekdays':weekdays,
        'validateWeekdays': validateWeekdays,
    })


def eventBooked(request):
    user = request.user
    times = [
        '2PM', '5.30PM'
    ]
    today = datetime.now()
    minDate = today.strftime('%d-%m-%Y')
    maxDate = strdeltatime

    day = request.session.get('day')
    event_type = request.session.get('event_type')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get('time')
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
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
            messages.success(request, "Please Select A Service!")

    return render(request, 'event_booked.html', {
        'times':hour,
    })


def userPanel(request):
    user = request.user
    appointments = Events.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'events':events,
    })


def userUpdateEvent(request, id):
    event = Events.objects.get(pk=id)
    userdatepicked = event.day
    today = datetime.today()
    minDate = today.strftime('%d-%m-%Y')

    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = validWeekday(22)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)


    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['event_type'] = event_type

        return redirect('userUpdateEventSubmit', id=id)


    return render(request, 'user_update_event.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'id': id,
        })



