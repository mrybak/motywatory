from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from motywatory.models import Motivator

class MotivatorForm(ModelForm):
    class Meta:
        model = Motivator
        fields = ('text', 'img', )

class UpdateUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

