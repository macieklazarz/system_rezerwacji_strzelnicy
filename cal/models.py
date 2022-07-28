from django.db import models
from django.urls import reverse
from users.models import User
from core.models import Tor


CHOICES = (
    (9, "09:00"),
    (10, "10:00"),
    (11, "11:00"),
    (12, "12:00"),
    (13, "13:00"),
    (14, "14:00"),
    (15, "15:00"),
    (16, "16:00"),
    (17, "17:00"),
    (18, "18:00"),
)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour_start = models.IntegerField(choices=CHOICES, verbose_name="Godzina początkowa")
    hour_stop = models.IntegerField(choices=CHOICES, verbose_name="Godzina końcowa")
    tor = models.ForeignKey(Tor, on_delete=models.CASCADE)

    def get_html_url(self, *args, **kwargs):
        url = reverse(
            "cal:event_delete",
            args=(
                self.id,
                kwargs["tor_id"],
            ),
        )
        return f'<a href="{url}"> {self.hour_start}:00 - {self.hour_stop}:00 </a>'

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day} {self.hour_start}:00 - {self.hour_stop}:00 {self.user}"
