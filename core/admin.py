from django.contrib import admin

from .models import State, City, AddressType, Address

class CityInline(admin.TabularInline):
    '''Tabular Inline View for City'''

    model = City
    min_num = 0
    extra = 1

class AddressInline(admin.TabularInline):
    '''Tabular Inline View for Address'''

    model = Address
    min_num = 0
    extra = 1

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    '''Admin View for State'''

    list_display = ('name', 'acronym')
    inlines = [
        CityInline,
    ]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for City'''

    list_display = ('name','ibge_number', 'state')
    list_filter = ('state',)
    inlines = [
        AddressInline,
    ]
    ordering = ('state',)

@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    '''Admin View for AddressType'''

    list_display = ('name',)