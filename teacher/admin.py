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
>>>>>>> ee2e9db (add, configurate and edit app teacher)
