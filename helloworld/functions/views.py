from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person

def index(request):
    person_list = Person.objects.all()
    template = loader.get_template('functions/index.html')
    context = {
        'person_list': person_list,
    }
    return HttpResponse(template.render(context, request))