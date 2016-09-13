from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from .views import home


class HomePageTest(TestCase):

    def test_root_url_resolve_home_index(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_view_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('index.html', request=request)
        self.assertEqual(response.content.decode(), expected_html)
