from django.db import models
from django.contrib.auth.models import User
 
class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=500)
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name

class MultipleChoiceTest(models.Model):
    test_name = models.CharField(max_length= 50) 
    test_description = models.CharField(max_length=500)
    def __str__(self):
        return self.test_name

class MultipleChoiceQuestion(models.Model):
    test = models.ForeignKey(MultipleChoiceTest, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 200)
    def __str__(self): 
        return self.question_text 

class MultipleChoiceChoice(models.Model): 

    class answer_choice(models.TextChoices):
        RIGHT = ('Richtig')
        FALSE = ('Falsch')

    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_answer_right = models.CharField(max_length=10, choices=answer_choice.choices, default=answer_choice.FALSE)
    def __str__(self): 
        return self.choice_text