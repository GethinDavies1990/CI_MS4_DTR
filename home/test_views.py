from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view(self):
        """
        Test that the index page is rendered correctly
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
