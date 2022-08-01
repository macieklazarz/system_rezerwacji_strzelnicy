from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import Register



class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, Register)