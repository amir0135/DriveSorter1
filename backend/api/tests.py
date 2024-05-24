from django.test import TestCase
from django.urls import reverse

class ApiTests(TestCase):
    def test_file_list(self):
        response = self.client.get(reverse('file-list'))
        self.assertEqual(response.status_code, 200)
