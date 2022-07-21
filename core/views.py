from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.shortcuts import render
from . models import Tor
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
	return render(request, 'core/home.html', {'title': 'Home', 'tory':Tor.objects.all()})

def about(request):
	return render(request, 'core/about.html')


class TorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = Tor
	template_name = 'core/tory_list.html'
	context_object_name = 'tory'

	def test_func(self):
		return self.request.user.is_staff

class TorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Tor
	template_name = 'core/tor_form.html'
	fields = ['nazwa', 'opis']


	def get_success_url(self):
		return reverse('tory_list')


	def test_func(self):
		return self.request.user.is_staff


class TorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Tor
	template_name = 'core/tor_form.html'
	fields = ['nazwa', 'opis']

	def get_success_url(self):
		return reverse('tory_list')


	def test_func(self):
		return self.request.user.is_staff


class TorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tor
	template_name = 'core/tor_delete_confirm.html'

	def get_success_url(self):
		return reverse('tory_list')


	def test_func(self):
		return self.request.user.is_staff