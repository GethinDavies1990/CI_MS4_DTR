from django.shortcuts import render

def profile(request):
    """ Display user's Profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
