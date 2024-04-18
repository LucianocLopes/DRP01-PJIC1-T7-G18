from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''

    list_display = ('full_name', 'email', 'phone_number')
