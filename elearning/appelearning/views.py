from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, get_list_or_404


from .models import MultipleChoiceTest, MultipleChoiceQuestion, MultipleChoiceChoice, Courses
from .forms import CreateMultiplechoiceTestForm, CreateQuestionForm, CreateCourseForm

# Index View
class IndexView(LoginView):
    template_name = 'appelearning/index.html'

# Passwort vergessen View --> Index View
class PasswordResetedView(PasswordResetView):
    template_name = 'appelearning/password_reset.html'
    success_url = reverse_lazy('appelearning:password_reset_done')
    email_template_name = 'appelearning/password_reset_email.html'

# Passwort wurde erfolgreich zurückgesetzt View --> Passwort vergessen View
class PasswordResetedDoneView(PasswordResetDoneView):
    template_name = 'appelearning/password_reset_done.html'


# Nutzer hinzufügen --> Menü
class CreateUserView(CreateView):
    template_name = 'appelearning/adduser.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('appelearning:overview')

# Nutzer Bearbeiten --> Menü
class UpdateUserView(UpdateView):
    template_name = 'appelearning/updateuser.html'
    model = User
    fields = "__all__"
   # form_class = UserChangeForm
    success_url = reverse_lazy('appelearning:overview')

# Nutzer ausloggen --> Menü
class LougoutView(LogoutView):
    template_name = 'appelearning/index.html'

# Overview View 
# Anzeige Navigation und übersicht der Tests / Test anlegen / Test bearbeiten 
class OverviewView(generic.ListView):
    template_name = 'appelearning/overview.html'
    model = Courses
    context_object_name = 'course_list'  

# Kurs hinzufügen
class CreateCourseView(CreateView):
    template_name = 'appelearning/add_course.html'
    form_class = CreateCourseForm
    success_url = reverse_lazy('appelearning:overview')

# Kurs bearbeiten
class UpdateCourseView(UpdateView):
    template_name = 'appelearning/update_course.html'
    model = Courses
    fields = "__all__"
    success_url = reverse_lazy('appelearning:overview')

class DeleteCourseView(DeleteView):
    template_name = 'appelearning/delete_course.html'
    model = Courses
    success_url = reverse_lazy('appelearning:overview')

# Kurs Profilseite
class ProfileCourseView(generic.DetailView):
    template_name = 'appelearning/course_profile.html'
    model = Courses


class CreateTestView(CreateView):
    fields = "__all__"
    template_name = 'appelearning/createtest.html'
    model = MultipleChoiceTest
    success_url = reverse_lazy('appelearning:overview')  

# Test lösen
class MakeTestView(generic.DetailView):
    template_name = 'appelearning/make_test.html'
    model = MultipleChoiceTest

# Test Lösungen überprüfen
def checkSolutions(request):
    question = get_list_or_404(MultipleChoiceQuestion)
    length = len(question)
    i = 0
    j = 10
    count_points = 0
    
    while i < length:
        try:
            selected_choice = question[i].multiplechoicechoice_set.get(pk = request.POST['choice%d' % j ])

        except (KeyError, MultipleChoiceChoice.DoesNotExist):
            return render(request, 'appelearning/make_test.html',
            {
                'error_message': "Du musst den ganzen Test ausfüllen",
            })
        
        else:
            if selected_choice.is_answer_right == 'Richtig':
                count_points += 1
            else:
               count_points -= 1
            selected_choice.save()
            i += 1
            j += 1

    return render(request, 'appelearning/show_results.html',{'points': count_points})


# Test Profil Seite --> Test starten
class MulitpleChoiceTestProfileView(generic.DetailView):
    template_name = 'appelearning/test_profile.html'
    model = MultipleChoiceTest


# Test Ergebnis ausgeben
class ShowResultsView (generic.ListView):
    template_name = 'appelearning/show_results.html'
    model = MultipleChoiceChoice
 
# Alle Tests anzeigen
class ShowTestsView(generic.ListView):
    template_name = 'appelearning/all_tests.html'
    model = MultipleChoiceTest
    context_object_name = 'test_list'

class ShowQuestionView(generic.ListView):
    template_name = 'appelearning/question_profile.html'
    model = MultipleChoiceQuestion
    context_object_name = 'question_list'