from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import home, about, TorListView, TorCreateView, TorUpdateView, TorDeleteView
from django.contrib.auth import views as auth_views
from users.views import Profile



class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, home)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_profile_url_resolves(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func.view_class, Profile)

    def test_tory_list_url_resolves(self):
        url = reverse("tory_list")
        self.assertEquals(resolve(url).func.view_class, TorListView)


    def test_tor_create_url_resolves(self):
        url = reverse("tor_create")
        self.assertEquals(resolve(url).func.view_class, TorCreateView)

    def test_tor_update_url_resolves(self):
        url = reverse("tor_update", args=[1])
        self.assertEquals(resolve(url).func.view_class, TorUpdateView)

    def test_tor_delete_url_resolves(self):
        url = reverse("tor_delete", args=[1])
        self.assertEquals(resolve(url).func.view_class, TorDeleteView)