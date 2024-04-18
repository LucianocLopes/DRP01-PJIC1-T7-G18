from django.contrib import admin

<<<<<<< HEAD
from .models import *

# INLINE
class PhoneSchoolInline(admin.TabularInline):
    '''Tabular Inline View for PhoneSchool'''

    model = PhoneSchool
    min_num = 1
    max_num = 3
    extra = 0

class AddressSchoolInline(admin.TabularInline):
    '''Tabular Inline View for AddressSchool'''

    model = AddressSchool
    min_num = 0
    max_num = 1


class TurnSchoolInline(admin.TabularInline):
    '''Tabular Inline View for TurnSchool'''

    model = TurnSchool
    max_num = 4
    extra = 0

class ClassRoomInline(admin.TabularInline):
    '''Tabular Inline View for ClassRoom'''

    model = ClassRoom
    min_num = 0
    extra = 0


class SchoolYearInline(admin.TabularInline):
    '''Tabular Inline View for SchoolYear'''

    model = SchoolYear
    min_num = 0
    extra = 1


# ADMIN_VIEW
=======
from .models import School, StructSchool


class StructSchoolInline(admin.TabularInline):
    '''Tabular Inline View for StructSchool'''

    model = StructSchool
    min_num = 1
    max_num = 20
    extra = 1


>>>>>>> 70b58ba (add app school and config pages)
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    '''Admin View for School'''

<<<<<<< HEAD
    list_display = ('name','fantasy_name', 'email', )
    inlines = [
        PhoneSchoolInline,
        AddressSchoolInline,
        TurnSchoolInline,
        ClassRoomInline,
        SchoolYearInline,
    ]
    
@admin.register(AddressSchool)
class AddressSchoolAdmin(admin.ModelAdmin):
    '''Admin View for School'''

    list_display = ('school', 'get_zip_code','get_address', 'number', 'complement', 'get_city_state' )


@admin.register(PhoneSchool)
class PhoneSchoolAdmin(admin.ModelAdmin):
    '''Admin View for School'''

    list_display = ('school','phone_type','get_phone',)
=======
    list_display = ('id', 'name', 'email')
    inlines = [
        StructSchoolInline,
    ]
>>>>>>> 70b58ba (add app school and config pages)
