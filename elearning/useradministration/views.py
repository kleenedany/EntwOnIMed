from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import User
from .forms import LoginForm

class IndexView(FormView):
    template_name = 'useradministration/index.html'
    context_object_name = 'user_list'
    form_class = LoginForm
    success_url = reverse_lazy('useradministration:profile')
    
   # def form_valid(self, form):

      #  return super().form_valid(form)
    
class ProfileView(generic.DetailView):
    model = User
    template_name = 'useradministration/profile.html'
