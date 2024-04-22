from django.contrib import admin

from .models import Discipline, Graduation

# Register your models here.


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    '''Admin View for Discipline'''

    list_display = ('id', 'name', 'duration')


@admin.register(Graduation)
class GraduationAdmin(admin.ModelAdmin):
    '''Admin View for Graduation'''

    list_display = ('name', 'duration_hours')
