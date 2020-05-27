from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_name']}),
        (None, {'fields': ['user_image']}),
        (None,  {'fields': ['password']}),
        (None, {'fields': ['first_name']}),
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['e_mail']}),
        ('Date information', {'fields': ['date_of_birth']}),
        (None, {'fields': ['gender']}),
        (None, {'fields': ['street']}),
        (None, {'fields': ['house_number']}),
        (None, {'fields': ['post_code']}),
        (None, {'fields': ['domicile']}),
    ]

    list_display = ('last_name', 'first_name')

admin.site.register(User, UserAdmin)