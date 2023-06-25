from django.shortcuts import render, get_object_or_404

from .models import Teams

def meet_the_team(request):
    """
    A view to show all staff members
    """
    teams = Teams()

    context = {
        'teams': teams,
    }

    return render(request, 'meet_the_team.html', context)
