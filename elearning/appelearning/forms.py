from django import forms

from .models import MultipleChoiceTest, MultipleChoiceQuestion, MultipleChoiceChoice, Courses

class CreateMultiplechoiceTestForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceTest
        fields = "__all__"

class CreateQuestionForm(forms.ModelForm):
    class Meta: 
        model = MultipleChoiceQuestion
        fields = "__all__"
        test = forms.ModelMultipleChoiceField(queryset=MultipleChoiceTest.objects.all())

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"