# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
urlpatterns = [
    path("meet_the_team/", views.meet_the_team, name="meet_the_team"),
    path("how_we_started/", views.how_we_started, name="how_we_started"),
    path("add/", views.add_team_member, name="add_team_member"),
    path("edit/<int:teams_id>/", views.edit_team_member, name="edit_team_member"),
    path("delete/<int:teams_id>/", views.delete_team_member, name="delete_team_member"),
]
