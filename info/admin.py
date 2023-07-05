# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Teams

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TeamsAdmin(admin.ModelAdmin):
    """
    Admin class for the Teams Model
    """

    class Meta:
        verbose_name = "Teams"
        verbose_name_plural = "Teams"

    list_display = (
        "full_name",
        "role",
        "about",
        "image",
    )


admin.site.register(Teams, TeamsAdmin)
