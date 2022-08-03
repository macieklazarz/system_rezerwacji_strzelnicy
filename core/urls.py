from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="about"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.ProfileView.as_view(), name="profile"),
    path("tory_list/", views.TorListView.as_view(), name="tory_list"),
    path("tory_list/new/", views.TorCreateView.as_view(), name="tor_create"),
    path("tory_list/update/<int:pk>", views.TorUpdateView.as_view(), name="tor_update"),
    path("tory_list/delete/<int:pk>", views.TorDeleteView.as_view(), name="tor_delete"),
]
