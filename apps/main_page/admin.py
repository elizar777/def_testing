from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (Employee,
                     Counter)


class EmployeeAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ky', {'fields': ('name_ky', 'position_ky', 'image', 'category')}),
        (u'Ru', {'fields': ('name_ru', 'position_ru')}),
        (u'En', {'fields': ('name_en', 'position_en')}),
    ]

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Counter)
