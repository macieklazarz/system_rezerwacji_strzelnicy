from django.forms import ModelForm, DateInput
from cal.models import Event
from users.models import User
from django.core.exceptions import ValidationError



class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ('user', 'year', 'month', 'day', 'hour_start', 'hour_stop', 'tor')

  def clean(self):
    cleaned_data = super().clean()
    if not cleaned_data.get('year'):
      raise ValidationError('Nie wybrano roku')
    elif not cleaned_data.get('month'):
      raise ValidationError('Nie wybrano miesiąca')
    elif not cleaned_data.get('day'):
      raise ValidationError('Nie wybrano dnia')
    elif not cleaned_data.get('user'):
      raise ValidationError('Nie wybrano usera')
    elif not cleaned_data.get('hour_start'):
      raise ValidationError('Nie wybrano godziny początkowej')
    elif not cleaned_data.get('hour_stop'):
      raise ValidationError('Nie wybrano godziny końcowej')
    elif cleaned_data.get('hour_start') >= cleaned_data.get('hour_stop'):
      raise ValidationError('Wprowadzono nieprawidłowe dane')


    check_date = Event.objects.filter(year = cleaned_data.get('year'), month = cleaned_data.get('month'), day = cleaned_data.get('day'), tor = cleaned_data.get('tor'))
    for date in check_date:
      if cleaned_data.get('hour_start') >= date.hour_start and cleaned_data.get('hour_stop') <= date.hour_stop:
        raise ValidationError(f'Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 1 - {date}')
      if cleaned_data.get('hour_start') <= date.hour_start and cleaned_data.get('hour_stop') >= date.hour_stop:
        raise ValidationError(f'Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 2 - {date}')
      if cleaned_data.get('hour_start') >= date.hour_start and cleaned_data.get('hour_start') < date.hour_stop:
        raise ValidationError(f'Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 3 - {date}')
      if cleaned_data.get('hour_stop') > date.hour_start and cleaned_data.get('hour_stop') <= date.hour_stop:
        raise ValidationError(f'Nie możesz dokonać rezerwacji ponieważ wybrany termin jest już zajety - var 4 - {date}')




  def __init__(self, *args, **kwargs):
    from django.forms.widgets import HiddenInput

    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['user'].widget = HiddenInput()
    self.fields['tor'].widget = HiddenInput()
    self.fields['year'].widget = HiddenInput()
    self.fields['month'].widget = HiddenInput()
    self.fields['day'].widget = HiddenInput()

