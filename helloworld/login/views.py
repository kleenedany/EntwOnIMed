from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .models import User
from .forms import LoginForm


class IndexView(LoginView):
    template_name = 'login/index.html'
   # form = LoginForm()
    #redirect_field_name = 'login:index'
    authentication_form= LoginForm

class WelcomeView(generic.ListView):
    model = User
    template_name = 'login/welcome.html'