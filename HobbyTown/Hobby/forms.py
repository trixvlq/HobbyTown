from captcha.fields import CaptchaField
from django import forms

from .models import *


class EventSignForm(forms.ModelForm):
    number = PhoneNumberField(region="KZ")
    def __init__(self, *args, **kwargs):
        games = kwargs.pop('games', None)
        super(EventSignForm, self).__init__(*args, **kwargs)
        if games:
            self.fields['games'].queryset = games.filter(players__gt=0)

    class Meta:
        model = EventSign
        fields = ["name", "number", "games", "game","event"]
        widgets = {
            'name': forms.TextInput(attrs={"type": "text", "placeholder": "Введите свое имя"}),
        }
