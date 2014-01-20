from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseRedirect

from motywatory import recaptcha
from motywatory.models import Motivator
from motywatory.forms import MotivatorForm

def index(request):
    motivators = Motivator.objects.all().order_by('created_on').reverse()
    return render(request, 'index.html', {'motivators': motivators})

class AddView(FormView):
    template_name = 'add.html'
    form_class = MotivatorForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        print self.request.POST
        RecaptchaRsp = recaptcha.submit(self.request.POST['recaptcha_challenge_field'], \
        self.request.POST['recaptcha_response_field'], '6LcLO-0SAAAAAMZKja_hev3pXpSDooEJ7iH-QQyp', '')
        if RecaptchaRsp.is_valid:
            print "valid"
            form.instance.author = self.request.user
            form.save()
            return super(AddView, self).form_valid(form)
        else:
            print "not valid"
            return self.form_invalid(form)

