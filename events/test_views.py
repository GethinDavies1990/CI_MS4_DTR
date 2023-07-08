# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BookEventViewTest(TestCase):
    def test_book_event_view(self):
        """
        Test that the events page is rendered correctly
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)
        response = self.client.get(reverse('book_event'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_event.html')


class EventBookedViewTest(TestCase):
    def test_event_booked_view(self):
        """
        Test that the events page is rendered correctly
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)
        response = self.client.get(reverse('event_booked'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_booked.html')
