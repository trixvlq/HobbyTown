from django import forms

from .models import *


class GameSignForm(forms.ModelForm):
    number = PhoneNumberField(region="KZ")
    def __init__(self, *args, **kwargs):
        games = kwargs.pop('games', None)
        super(GameSignForm, self).__init__(*args, **kwargs)
        if games:
            self.fields['games'].queryset = games.filter(players__gt=0)

    class Meta:
        model = SpecialSign
        fields = ["name", "number", "games", "game","event"]
        widgets = {
            'name': forms.TextInput(attrs = {"type": "text", "placeholder": "Введите свое имя"}),
            'number': forms.TextInput(attrs = {"type": "number", "placeholder": "Введите номер телефона"}),
        }
class EventSignForm(forms.ModelForm):
    number = PhoneNumberField(region="KZ")
    def __init__(self, *args, **kwargs):
        games = kwargs.pop('games', None)
        super(EventSignForm, self).__init__(*args, **kwargs)
        if games:
            self.fields['games'].queryset = games.filter(players__gt=0)

    class Meta:
        model = SpecialSign
        fields = ["name", "number", "games", "game","event"]
        widgets = {
            'name': forms.TextInput(attrs = {"type": "text", "placeholder": "Введите свое имя"}),
            'number': forms.TextInput(attrs = {"type": "number", "placeholder": "Введите номер телефона"}),
        }
