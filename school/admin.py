from django.contrib import admin

from .models import School, StructSchool


class StructSchoolInline(admin.TabularInline):
    '''Tabular Inline View for StructSchool'''

    model = StructSchool
    min_num = 1
    max_num = 20
    extra = 1


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    '''Admin View for School'''

    list_display = ('id', 'name', 'email')
    inlines = [
        StructSchoolInline,
    ]
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(SchoolAdmin, self).save_model(request, obj, form, change)
