from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(View):
    def get(self, *args, **kwargs):
        form = UserRegisterForm()
        profile_form = ProfileUpdateForm()
        return render(
            self.request,
            "users/register.html",
            {"form": form, "profile_form": profile_form},
        )

    def post(self, *args, **kwargs):
        form = UserRegisterForm(self.request.POST)
        profile_form = ProfileUpdateForm(self.request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            profil = Profile.objects.get(user__username=username)
            profil.imie = profile_form.cleaned_data.get("imie")
            profil.nazwisko = profile_form.cleaned_data.get("nazwisko")
            profil.nr_telefonu = profile_form.cleaned_data.get("nr_telefonu")
            profil.save()

            messages.success(self.request, f"Dodano konto dla {username}")
            return redirect("login")
        return render(
            self.request,
            "users/register.html",
            {"form": form, "profile_form": profile_form},
        )

class ProfileView(View, LoginRequiredMixin):
    def get(self, *args, **kwargs):
        user_form = UserUpdateForm(instance=self.request.user)
        profile_form = ProfileUpdateForm(instance=self.request.user.profile)
        return render(
            self.request,
            "users/profile.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, *args, **kwargs):
        user_form = UserUpdateForm(self.request.POST, instance=self.request.user)
        profile_form = ProfileUpdateForm(
            self.request.POST, instance=self.request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(self.request, "Twój profil został uaktualniony")
            return redirect("profile")
        return render(
            self.request,
            "users/profile.html",
            {"user_form": user_form, "profile_form": profile_form},
        )
