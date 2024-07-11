from modeltranslation.translator import translator, TranslationOptions
from apps.structure.models import Block,Department


class BlockTranslationOptions(TranslationOptions):
    fields = ('title',) 

translator.register(Block, BlockTranslationOptions)

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name','description') 

translator.register(Department, DepartmentTranslationOptions)