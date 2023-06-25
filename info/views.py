from django.shortcuts import render


def meet_the_team(request):
    """
    A view to show all staff members
    """

    return render(request, 'info/meet_the_team.html')