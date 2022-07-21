from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		profile_form = ProfileUpdateForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			profil = Profile.objects.get(user__username=username)
			profil.imie = profile_form.cleaned_data.get('imie')
			profil.nazwisko = profile_form.cleaned_data.get('nazwisko')
			profil.nr_telefonu = profile_form.cleaned_data.get('nr_telefonu')
			profil.save()

			messages.success(request, f'Dodano konto dla {username}')
			return redirect('login')
	else:
		form = UserRegisterForm()
		profile_form = ProfileUpdateForm()

	return render(request, 'users/register.html', {'form':form, 'profile_form':profile_form})

@login_required
def profile(request):
	if request.method=='POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Twój profil został uaktualniony')
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	return render(request, 'users/profile.html', {'user_form':user_form, 'profile_form':profile_form})