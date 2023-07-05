# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Events

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EventsAdmin(admin.ModelAdmin):
    """
    Admin class for the Events model
    """

    class Meta:
        """
        Class for the Meta object for events
        """

        verbose_name_plural = "Events"

    list_display = ("user", "event_type", "day", "time", "time_ordered")


admin.site.register(Events, EventsAdmin)
