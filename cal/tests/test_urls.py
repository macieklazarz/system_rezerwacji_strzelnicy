from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cal.views import get_date, CalendarView, EventNew, EventDetail, EventDelete



class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('cal:index')
        self.assertEquals(resolve(url).func, get_date)

    def test_calendar_url_resolves(self):
        url = reverse('cal:calendar', args=[1])
        self.assertEquals(resolve(url).func.view_class, CalendarView)

    def test_event_newer_url_resolves(self):
        url = reverse('cal:event_newer', args=[1,1,1,2022])
        self.assertEquals(resolve(url).func.view_class, EventNew)

    def test_event_detail_url_resolves(self):
        url = reverse('cal:event_detail', args=[1,1])
        self.assertEquals(resolve(url).func.view_class, EventDetail)

    def test_event_delete_url_resolves(self):
        url = reverse('cal:event_delete', args=[1,1])
        self.assertEquals(resolve(url).func.view_class, EventDelete)