from django.contrib import admin

from .models import Graduation, Discipline


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    '''Admin View for Discipline'''

    list_display = ('name',)


@admin.register(Graduation)
class GraduationAdmin(admin.ModelAdmin):
    '''Admin View for Graduation'''

    list_display = ('name', 'school',)