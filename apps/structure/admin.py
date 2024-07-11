from django.contrib import admin
from django.contrib.auth.models import  Group
from apps.structure.models import Block , Department
from modeltranslation.admin import TranslationAdmin

class BlockAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ky', {'fields': ('title_ky', 'photo_url' )}),
        (u'Ru', {'fields': ('title_ru', )}),
        (u'En', {'fields': ('title_en', )}),
    ]

admin.site.register(Block, BlockAdmin)


class DepartmentAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ky', {'fields': ('name_ky', 'description_ky','photo_url', 'block')}),
        (u'Ru', {'fields': ('name_ru', 'description_ru', )}),
        (u'En', {'fields': ('name_en', 'description_en', )}),
    ]

admin.site.register(Department, DepartmentAdmin)



admin.site.unregister(Group)