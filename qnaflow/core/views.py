from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import signUpForm,UserForm
# Create your views here.

def index(request):
    return render(request,"index.html")

class SignUp2(CreateView):
    form_class=signUpForm
    success_url=reverse_lazy('index')
    template_name='core/signup2.html'

class SignUp1(CreateView):
    form_class=UserForm
    success_url=reverse_lazy('index')
    template_name='core/signup1.html'
