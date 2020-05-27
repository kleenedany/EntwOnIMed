from django.contrib import admin

from .models import User

class LoginAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Login', {
            'fields': ('user_name', 'password')
        }),
    )
admin.site.register(User, LoginAdmin)
