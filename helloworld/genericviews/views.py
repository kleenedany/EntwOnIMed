from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


from .models import Person, PersonalInformation
from .forms import CreatePersonForm, CreatePersonalInformationForm

class IndexView(generic.ListView):
     template_name = 'genericviews/index.html'
     context_object_name = 'person_list'

     def get_queryset(self):
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = PersonalInformation
    template_name = 'genericviews/detail.html'

class CreatePersonView(CreateView):
    model = Person
    fields = "__all__"
    template_name = 'genericviews/form.html'
    success_url = reverse_lazy('genericviews:index')

#class CreatePersonView(FormView):
#    template_name = 'genericviews/form.html'
#    form_class = CreatePersonForm
#    success_url = reverse_lazy('genericviews:index')

#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)

#def createPersonForm(request):
#    if request.method == 'POST':
#        form = CreatePersonForm(request.POST)

#        if form.is_valid():
#           form.save()
#           return HttpResponseRedirect(reverse_lazy('genericviews:index'))
#    else:
#       form = CreatePersonForm()
#    return render(request, 'genericviews/form.html', {'form': form})

class DeletePersonView(DeleteView):
    model = Person
    template_name = 'genericviews/delete.html'
    success_url = reverse_lazy('genericviews:index')

class UpdatePersonView(UpdateView):
    model = Person
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('genericviews:index')