from django.contrib import admin
from .models import Events

# Register your models here.

class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'event_type',
        'day',
        'time',
        'time_ordered'
    )


admin.site.register(Events, EventsAdmin)
