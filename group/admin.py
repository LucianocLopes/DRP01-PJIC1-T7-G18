from django.contrib import admin

from .models import Group

# Register your models here.


@admin.register(Group)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('name',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(StudentAdmin, self).save_model(request, obj, form, change)
