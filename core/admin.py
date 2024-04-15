from django.contrib import admin
<<<<<<< HEAD

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
=======
from .models import Cidade, Estado, Lougradouro


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    '''Admin View for Cidade'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


class CidadeInline(admin.TabularInline):
    '''Tabular Inline View for Cidade'''

    model = Cidade
    min_num = 0
    max_num = 0
    extra = 1
    # raw_id_fields = (,)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    '''Admin View for Estado'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        CidadeInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
# Register your models here.


@admin.register(Lougradouro)
class LougradouroAdmin(admin.ModelAdmin):
    '''Admin View for Lougradouro'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
>>>>>>> a8c0174 (include core app and configs)
