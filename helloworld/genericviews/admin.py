from django.contrib import admin

from .models import Person, PersonalInformation

class PersonalInformationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Angaben zur Person', {
            'fields': ('person', 'street', 'number', 'postcode', 'domicile')
        }),
    )
admin.site.register(PersonalInformation, PersonalInformationAdmin)

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Person', {
            'fields': ('last_name', 'first_name')
        }),
    )

    list_display = ('last_name', 'first_name')

admin.site.register(Person, PersonAdmin)
