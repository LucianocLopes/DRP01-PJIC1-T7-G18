from django.contrib import admin

from .models import GridGroup, Group


class GridGroupInline(admin.TabularInline):
    '''Tabular Inline View for GridGroup'''

    model = GridGroup
    min_num = 1
    extra = 1

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    '''Admin View for Group'''

    list_display = ('graduation',)
    # list_filter = ('',)
    inlines = [
        GridGroupInline,
    ]

