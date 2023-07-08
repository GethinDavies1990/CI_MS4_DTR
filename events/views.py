# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Internal:
from .models import Events
from profiles.models import UserProfile

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

strdeltatime = ""
date = ""


@login_required
def book_event(request):
    """
    A function to show the book event options and dates
    """
    weekdays = valid_weekday(60)
    validate_weekdays = is_weekday_valid(weekdays)

    if request.method == "POST":
        event_type = request.POST.get("event_type")
        day = request.POST.get("day")
        if event_type is None:
            messages.warning(request, "Please select an event type!")
            return redirect("book_event")

        request.session["day"] = day
        request.session["event_type"] = event_type

        return redirect("event_booked")

    return render(
        request,
        "book_event.html",
        {
            "weekdays": weekdays,
            "validate_weekdays": validate_weekdays,
        },
    )


@login_required
def event_booked(request):
    """
    A function to book the event
    """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        times = ["2PM", "5.30PM"]
        today = datetime.now()
        min_date = today.strftime("%Y-%m-%d")
        max_date = (today + timedelta(days=60)).strftime("%Y-%m-%d")

        day = request.session.get("day")
        event_type = request.session.get("event_type")

        hour = check_time(times, day)
        if request.method == "POST":
            time = request.POST.get("time")
            date = day_to_weekday(day)

            if event_type is not None:
                if day <= max_date and day >= min_date:
                    if (
                        date == "Thursday"
                        or date == "Friday"
                        or date == "Saturday"
                        or date == "Sunday"
                    ):
                        if Events.objects.filter(day=day).count() < 11:
                            if Events.objects.filter(
                                    day=day, time=time).count() < 1:
                                EventsForm = Events.objects.get_or_create(
                                    user=user,
                                    event_type=event_type,
                                    day=day,
                                    time=time,
                                )
                                messages.success(request, "Event Booked")
                                return redirect("home")
                            else:
                                messages.warning(
                                    request, "The Selected"
                                    "Time Has Been Reserved Before!", )
                        else:
                            messages.warning(
                                request, "The Selected Day Is Full!")
                    else:
                        messages.warning(
                            request, "The Selected Date Is Incorrect")
                else:
                    messages.warning(
                        request, "The Selected Date"
                        "Isn't In The Correct Time Period!")
            else:
                messages.warning(request, "Please Select A event_type!")

        return render(
            request,
            "event_booked.html",
            {
                "times": hour,
            },
        )
    else:
        return redirect("login.html")


def day_to_weekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime("%A")
    return y


def valid_weekday(days):
    # Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime("%A")
        if (
            y == "Thursday"
            or date == "Friday"
            or date == "Saturday"
            or date == "Sunday"
        ):
            weekdays.append(x.strftime("%Y-%m-%d"))
    return weekdays


def is_weekday_valid(x):
    validate_weekdays = []
    for j in x:
        if Events.objects.filter(day=j).count() < 10:
            validate_weekdays.append(j)
    return validate_weekdays


def check_time(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Events.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x
