from django.shortcuts import render
from django.http import HttpResponse
from .  import forms
from django.views.generic.edit import FormView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(FormView):
    template_name = 'yt_form.html'
    form_class = forms.YTForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # url -> mp3
        form.getMp3()
        return super().form_valid(form)