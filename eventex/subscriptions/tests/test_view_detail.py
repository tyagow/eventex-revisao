from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Tiago Almeida', cpf='12345678901',
                   email='tyagow@hotmail.com.br', phone='48-9999-0000')
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.hashId))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.email, self.obj.cpf, self.obj.phone)
        with self.subTest():
            for content in contents:
                self.assertContains(self.resp, content)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('detail', '00000000-0000-0000-0000-000000000000'))  # modificado
        self.assertEqual(404, resp.status_code)