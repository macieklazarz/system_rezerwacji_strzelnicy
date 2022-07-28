from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.urls import reverse
import locale

locale.setlocale(locale.LC_ALL, "pl_PL")


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, tor_id=None, user=None):
        self.year = year
        self.month = month
        self.tor_id = tor_id
        self.user = user
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(day=day).order_by("hour_start")
        current_day = ""
        for event in events_per_day:
            if self.user.is_superuser or event.user == self.user:
                current_day += f'<li><span style="position:relative; left: -10px;"> {event.get_html_url(tor_id=self.tor_id)} </span></li>'
            else:
                current_day += f'<li><span style="position:relative; left: -10px;"> {event.hour_start}:00 - {event.hour_stop}:00</span></li>'

        url_to_event = reverse(
            "cal:event_newer", args=(self.tor_id, day, self.month, self.year)
        )
        url_string = f'<a href="{url_to_event}">{day}</a>'
        if day != 0:
            if current_day:
                return f"<td><br><span class='date'>{url_string}</span><br> <span>Rezerwacje:</span> <ul> {current_day} </ul></td>"

            return f"<td><span class='date'>{url_string}</span> <ul> {current_day} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events):
        week = ""
        for current_day, weekday in theweek:
            week += self.formatday(current_day, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(year=self.year, month=self.month, tor=self.tor_id)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"

        return cal
