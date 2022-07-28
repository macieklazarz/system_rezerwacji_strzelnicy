from django.forms import ModelForm, DateInput
from cal.models import Event
from users.models import User
from django.core.exceptions import ValidationError


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("user", "year", "month", "day", "hour_start", "hour_stop", "tor")

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput

        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["user"].widget = HiddenInput()
        self.fields["tor"].widget = HiddenInput()
        self.fields["year"].widget = HiddenInput()
        self.fields["month"].widget = HiddenInput()
        self.fields["day"].widget = HiddenInput()

    def clean(self):
        fields = {
            "year": "year",
            "month": "month",
            "day": "day",
            "user": "user",
            "hour_start": "godzina początkowa",
            "hour_stop": "godzina końcowa",
        }
        cleaned_data = super().clean()
        for key, value in fields.items():
            if not cleaned_data.get(key):
                raise ValidationError(f"Brak wartości dla pola {value}")

        current_date = Event.objects.filter(
            year=cleaned_data.get("year"),
            month=cleaned_data.get("month"),
            day=cleaned_data.get("day"),
            tor=cleaned_data.get("tor"),
        )
        self.check_date(current_date, cleaned_data)

    def check_date(self, current_date, selected_date):
        for date in current_date:
            if selected_date.get("hour_start") >= selected_date.get("hour_stop"):
                raise ValidationError(f"Nieprawidłowe godziny startu i zakończenia")
            if (
                selected_date.get("hour_start") >= date.hour_start
                and selected_date.get("hour_stop") <= date.hour_stop
            ):
                raise ValidationError(
                    f"Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 1 - {date}"
                )
            if (
                selected_date.get("hour_start") <= date.hour_start
                and selected_date.get("hour_stop") >= date.hour_stop
            ):
                raise ValidationError(
                    f"Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 2 - {date}"
                )
            if (
                selected_date.get("hour_start") >= date.hour_start
                and selected_date.get("hour_start") < date.hour_stop
            ):
                raise ValidationError(
                    f"Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 3 - {date}"
                )
            if (
                selected_date.get("hour_stop") > date.hour_start
                and selected_date.get("hour_stop") <= date.hour_stop
            ):
                raise ValidationError(
                    f"Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 4 - {date}"
                )
