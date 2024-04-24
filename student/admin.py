from django.contrib import admin

from .models import Student, RegisteredManager, StudentNoResgistred, StudentResgistred, NoRegisteredManager

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('first_name', 'registered')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(StudentAdmin, self).save_model(request, obj, form, change)


@admin.register(StudentResgistred)
class StudentRegisteredAdmin(StudentAdmin):
    '''Admin View for Student'''
    objects = RegisteredManager()

    class Meta:
        proxy = True


@admin.register(StudentNoResgistred)
class StudentNoRegisteredAdmin(StudentAdmin):
    '''Admin View for Student'''
    objects = NoRegisteredManager()

    class Meta:
        proxy = True
