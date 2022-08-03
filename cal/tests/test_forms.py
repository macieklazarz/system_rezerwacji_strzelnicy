from django.test import TestCase
from cal.forms import EventForm
from django.contrib.auth.models import User

class TestForms(TestCase):
    def test_event_form_valid(self):
        user_selected = User.objects.create(username='admin')
        form = EventForm(data={
            # "user": user_selected,
            "user": 1,
            "year": 2022,
            "month": 8,
            "day": 28,
            "hour_start": 11,
            "hour_stop": 15,
            "tor":1
        })

        self.assertTrue(form.is_valid())