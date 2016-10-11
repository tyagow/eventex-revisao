from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from .views import home


class HomePageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_view_returns_correct_html(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')


