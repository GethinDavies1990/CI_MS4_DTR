from django.shortcuts import render
from .models import Teams

def meet_the_team(request):
    """
    A view to show all staff members
    """
    teams = Teams.objects.all()  # Fetch all Teams objects from the database

    context = {
        'teams': teams,
    }

    return render(request, 'meet_the_team.html', context)


def how_we_started(request):
    """
    A view to render the how we started page
    """

    return render(request, 'how_we_started.html')

