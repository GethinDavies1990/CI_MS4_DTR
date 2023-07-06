# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.http import Http404
from django.shortcuts import render


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def page_not_found(request, exception):
    """
    Function to return the Error 404 page
    """
    return render(request, 'errors/404.html', status=404)


def server_error(request, exception=None):
    """
    Function to return the Error 500 page
    """
    return render(request, 'errors/500.html', status=500)


def bad_request(request, exception):
    """
    Function to return the Error 400 page
    """
    return render(request, 'errors/400.html', status=400)


def forbidden(request, exception):
    """
    Function to return the Error 403 page
    """
    return render(request, 'errors/403.html', status=403)
