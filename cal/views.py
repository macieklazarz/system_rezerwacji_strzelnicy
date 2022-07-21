from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from users.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
# from core.models import Tor

from .models import *
from .utils import Calendar
from .forms import EventForm

class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tor_id = self.kwargs['tor_id']
        # print(f'usr: {self.request.user}')

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month, tor_id, self.request.user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['tor_id'] = tor_id
        # context['user'] = self.request.user
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})


def event_new(request, event_id=None, tor_id=None, day=None, month=None, year=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    # print(f'tor id: {tor_id}')
    # print(f'day: {day}')

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        # print(f'form: {form}')
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar', kwargs={'tor_id':tor_id,}))
        # return reverse('cal:calendar', kwargs={'tor_id':tor_id})
    else:
        # print(User.objects.filter(id=1))
        us = User.objects.filter(id=1)
        # form = EventForm(form_kwargs={'user_kw':'blabla'}, instance=instance)
        form = EventForm(user=us)
        # pass

        # form.fields['user'].initial = User.objects.filter(id=1)
    return render(request, 'cal/event.html', {'form': form, 'tor_id':tor_id})


class EventNew(LoginRequiredMixin, CreateView):
    login_url='home'
    template_name='cal/event.html'
    form_class = EventForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        self.tor_id = self.kwargs['tor_id']
        self.day = self.kwargs['day']
        self.month = self.kwargs['month']
        self.year = self.kwargs['year']
        context['tor_id']= self.kwargs['tor_id']
        rezerwacje = Event.objects.filter(tor=self.kwargs['tor_id'], year=self.kwargs['year'], month=self.kwargs['month'], day=self.kwargs['day'])
        context['rezerwacje']=rezerwacje
        # print(f'rezerwacje: {rezerwacje}')

        return context

    def get_success_url(self):
        return reverse('cal:calendar', kwargs={'tor_id':self.kwargs['tor_id']})

    def get_initial(self, *args, **kwargs):
        initial = super(EventNew, self).get_initial()
        initial = initial.copy()
        initial['user']=self.request.user
        initial['day']=self.kwargs['day']
        initial['month']=self.kwargs['month']
        initial['year']=self.kwargs['year']
        initial['tor']=Tor.objects.filter(id=self.kwargs['tor_id'])[0]
        # print(f"tor: {Tor.objects.filter(id=self.kwargs['tor_id'])}")
        return initial


class EventDetail(LoginRequiredMixin, DetailView):
    login_url='home'
    template_name='cal/event_details.html'
    model = Event


class EventDelete(LoginRequiredMixin, DeleteView):
    login_url='home'
    template_name='cal/event_delete.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tor_pk'] = self.kwargs['tor_pk']
        return context

    def get_success_url(self):
        return reverse("cal:calendar", kwargs={'tor_id': self.kwargs['tor_pk']})


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or self.get_object().user == request.user:
            return super(EventDelete, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('<h1>Jestes nieuprawniony</h1>')



