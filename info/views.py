from django.shortcuts import render

from .models import Teams

def meet_the_team(request):
    """
    A view to show all staff members
    """
    teams = Teams.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'info/meet_the_team.html', context)