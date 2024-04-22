from django.contrib import admin

from .models import Discipline, Graduation

# Register your models here.


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    '''Admin View for Discipline'''

    list_display = ('id', 'name', 'duration')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(DisciplineAdmin, self).save_model(request, obj, form, change)


@admin.register(Graduation)
class GraduationAdmin(admin.ModelAdmin):
    '''Admin View for Graduation'''

    list_display = ('name', 'duration_hours')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(GraduationAdmin, self).save_model(request, obj, form, change)
