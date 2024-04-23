from django.contrib import admin

<<<<<<< HEAD
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

=======
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
>>>>>>> 93b9589 (add and config new app group)
