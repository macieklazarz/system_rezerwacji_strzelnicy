from django.test import TestCase
from django.urls import reverse
from cal.models import Event
from django.contrib.auth.models import User
from core.models import Tor



class TestViews(TestCase):

    def setUp(self):
        user_selected = User.objects.create(username='admin')
        tor_selected = Tor.objects.create(nazwa='name_of_tor')
        self.event = Event(
            user = user_selected,
            year = 2022,
            month = 1,
            day = 1,
            hour_start = 12,
            hour_stop = 13,
            tor = tor_selected
        )
    def test_str_method(self):
        self.assertEquals(self.event, '2022/1/1 12:00 - 13:00 admin')