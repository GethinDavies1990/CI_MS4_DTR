from django.shortcuts import render, redirect, reverse
from .models import Teams
from .forms import TeamsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def add_team_member(request):
    """ Add Team member to app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TeamsForm(request.POST, request.FILES)
        if form.is_valid():
            team_member = form.save()
            messages.success(request, 'Successfully added Team Member!')
            return redirect(reverse('meet_the_team'))
        else:
            messages.error(request, 'Failed to add Team member. Please ensure the form is valid')
    else:
        form = TeamsForm()

    template = 'add_team_member.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
