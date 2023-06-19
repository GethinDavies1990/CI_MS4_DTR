from django.shortcuts import render

def profile(request):
    """ Display user's Profile """
    template = 'profiles/profile.html'
    constext = {}

    return render(request, template, context)
