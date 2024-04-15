from django.contrib import admin
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
