from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import *

class CardForm(forms.ModelForm):

    class Meta:
        model = InsideBoard
        fields = '__all__'