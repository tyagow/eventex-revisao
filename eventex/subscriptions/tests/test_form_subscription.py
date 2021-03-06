from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = SubscriptionForm()
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_cpf_is_digit(self):
        """"CPF must only accept digits"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='tiago almeida')
        self.assertEqual('Tiago Almeida', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email="")
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone="")
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """email and phone are optional but one must br informed"""
        form = self.make_validated_form(phone="", email="")
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorMessage(self, form, field, msg):
        erros = form.errors
        erros_list = erros[field]
        self.assertListEqual([msg], erros_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Tiago Almeida', cpf='12345678901',
                    email='tyagow@hotmail.com.br', phone='48-9999-0000')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form