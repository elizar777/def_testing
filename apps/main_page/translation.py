from modeltranslation.translator import translator, TranslationOptions
from .models import (Employee)


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('position', 'name')

translator.register(Employee, EmployeeTranslationOptions)