from django.shortcuts import render
from django.views.generic.edit import FormView

from motywatory import recaptcha
from motywatory.models import Motivator
from motywatory.forms import MotivatorForm


def index(request):
    motivators = Motivator.objects.all().order_by('created_on').reverse()
    return render(request, 'index.html', {'motivators': motivators})

class add(FormView):
    template_name = 'add.html'
    form_class = MotivatorForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        print request.POST
        RecaptchaRsp = recaptcha.submit(request.POST['recaptcha_challenge_field'], \
        request.POST['recaptcha_response_field'], '6LcLO-0SAAAAAMZKja_hev3pXpSDooEJ7iH-QQyp', '')
        if RecaptchaRsp.is_valid:
            return super(ContactView, self).form_valid(form) 
        else:
            return False # todo - check this one

