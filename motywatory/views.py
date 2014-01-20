from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from jnp3.serializers import MotivatorSerializer

from motywatory import recaptcha
from motywatory import tasks
from motywatory.models import Motivator
from motywatory.forms import MotivatorForm, UpdateUserForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        if RecaptchaRsp.is_valid and form.is_valid():
            # form.instance.author = self.request.user
            tasks.upload_motivator.delay(form.cleaned_data.get('text'), form.cleaned_data.get('img'), self.request.user)
            return redirect('index')
        else:
            print "not valid"
            return self.form_invalid(form)


@api_view(['POST'])
def add_motivator(request):
    if request.method == 'POST':
        serializer = MotivatorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.object.author = request.user
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
def update_user(request):
    if request.POST:
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data.get('username')
            request.user.password = make_password(form.cleaned_data.get('password'))
            request.user.save()
            return redirect('index')
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'edit_user.html', {'form': form})
