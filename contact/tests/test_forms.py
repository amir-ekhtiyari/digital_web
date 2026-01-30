from django.test import TestCase

from contact.forms import ContactForm


class ContactFormTest(TestCase):
    def test_form_valid(self):
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "ali@example.com",
            "subject": "درخواست همکاری",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_email_required(self):
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "",
            "subject": "درخواست همکاری",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_form_subject_required(self):
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "ali@example.com",
            "subject": "",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("subject", form.errors)

    def test_form_message_required(self):
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "ali@example.com",
            "subject": "درخواست همکاری",
            "message": "",
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("message", form.errors)

    def test_form_save(self):
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "ali@example.com",
            "subject": "درخواست همکاری",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
        contact = form.save()
        self.assertEqual(contact.first_name, "علی")
        self.assertEqual(contact.last_name, "احمدی")
        self.assertEqual(contact.email, "ali@example.com")
        self.assertEqual(contact.subject, "درخواست همکاری")
        self.assertEqual(contact.message, "می‌خوام با شما همکاری کنم.")
