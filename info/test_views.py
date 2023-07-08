# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.urls import reverse

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class HowWeStartedViewTest(TestCase):
    def test_how_we_started_view(self):
        """
        Test that the events page is rendered correctly
        """
        response = self.client.get(reverse('how_we_started'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'how_we_started.html')


class MeetTheTeamViewTest(TestCase):
    def test_meet_the_team_view(self):
        """
        Test that the events page is rendered correctly
        """
        response = self.client.get(reverse('meet_the_team'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teams/meet_the_team.html')
