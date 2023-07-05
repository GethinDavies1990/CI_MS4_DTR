from django.shortcuts import render, redirect, reverse, get_object_or_404
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

    return render(request, 'teams/meet_the_team.html', context)


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

    template = 'teams/add_team_member.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_team_member(request, teams_id):
    """ Edit a Team member in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('meet_the_team'))

    teams = get_object_or_404(Teams, pk=teams_id)
    if request.method == 'POST':
        form = TeamsForm(request.POST, request.FILES, instance=teams)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Team Member!')
            return redirect('edit_team_member', teams_id=teams.id)
        else:
            messages.error(request, 'Failed to update team member. Please ensure the form is valid.')
    else:
        form = TeamsForm(instance=teams)
        messages.info(request, f'You are editing {teams.full_name}')

    template = 'teams/edit_team_member.html'
    context = {
        'form': form,
        'teams': teams,
    }

    return render(request, template, context)


@login_required
def delete_team_member(request, teams_id):
    """ Delete a team member in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    teams = get_object_or_404(Teams, pk=teams_id)
    teams.delete()
    messages.success(request, 'Team member Deleted!')
    return redirect(reverse('meet_the_team'))

