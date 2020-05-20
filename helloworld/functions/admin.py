from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['last_name']}),
    (None, {'fields': ['first_name']}),
    ]

    list_display = ('last_name', 'first_name')

admin.site.register(Person, PersonAdmin)