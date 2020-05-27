from django import forms

from .models import Person, PersonalInformation

class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class CreatePersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = "__all__"
        person =  forms.ModelMultipleChoiceField(queryset=Person.objects.all())