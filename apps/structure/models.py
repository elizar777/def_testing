from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Block(models.Model):
    title = models.CharField(max_length=255, verbose_name="Зогловок")
    photo_url = models.ImageField(upload_to='blocks/', verbose_name="Фото")

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отделения')
    description = RichTextField(verbose_name='Описание отделения')
    photo_url = models.ImageField(upload_to='department/', verbose_name="Фото")
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Блок')

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name
