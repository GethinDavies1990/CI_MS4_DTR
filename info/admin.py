from django.contrib import admin
from .models import Teams

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'about',
        'image',
    )


admin.site.register(Teams, TeamsAdmin)
