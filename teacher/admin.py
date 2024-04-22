from django.contrib import admin

<<<<<<< HEAD
from .models import *

# INLINE
class PhoneTeacherInline(admin.TabularInline):
    '''Tabular Inline View for PhoneSchool'''

    model = PhoneTeacher
    min_num = 0
    max_num = 3
    extra = 0

class AddressTeacherInline(admin.TabularInline):
    '''Tabular Inline View for AddressSchool'''

    model = AddressTeacher
    min_num = 0
    max_num = 1


# ADMIN_VIEW
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for School'''

    list_display = ('full_name', 'email',)
    inlines = [
        PhoneTeacherInline,
        AddressTeacherInline,
    ]

=======
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''

    list_display = ('full_name', 'email', 'phone_number')
<<<<<<< HEAD
>>>>>>> ee2e9db (add, configurate and edit app teacher)
=======
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(TeacherAdmin, self).save_model(request, obj, form, change)
>>>>>>> 8b7b00c (corrections in apps views, forms and templates)
