from .models import *
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSign
        fields = (
            "event","name","number","game",
        )