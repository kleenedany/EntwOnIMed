from django.contrib import admin

from .models import Courses, MultipleChoiceTest, MultipleChoiceQuestion, MultipleChoiceChoice

class CoursesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Kurs erstellen', {
            'fields': ('course_name', 'course_description', 'responsible_person')
        }), 
    )

admin.site.register(Courses, CoursesAdmin)



class MultipleChoiceChoiceInline(admin.TabularInline):
    model = MultipleChoiceChoice
    extra = 2

class MultipleChoiceTestAdmin(admin.ModelAdmin): 
    fieldsets = (
        ('Multiplechoice Test erstellen', {
            'fields': ('test_name', 'test_description')
        }),
    )
   
admin.site.register(MultipleChoiceTest, MultipleChoiceTestAdmin)

class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Fragen Multiple Choice Test', {
            'fields': ('test', 'question_text')
        }),
    )
    inlines = [MultipleChoiceChoiceInline]

admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)


