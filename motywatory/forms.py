form django.forms import ModelForm

from motywatory.models import Motivator

class MotivatorForm (ModelForm):
    class Meta:
        model = Motivator
        fields = ('text', )

