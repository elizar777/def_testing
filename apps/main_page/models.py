from django.core.exceptions import ValidationError
from django.db import models


class Employee(models.Model):
    CATEGORY_CHOICES = [
        ('directorate', 'Дирекция'),
        ('academic_council', 'Ученый совет'),
        ('employees', 'Сотрудники')
    ]

    image = models.ImageField(verbose_name='Изображение сотрудника',
                              upload_to='Сотрудники',
                              null=True,
                              blank=True)
    name = models.CharField(verbose_name='ФИО сотрудника',
                            max_length=50)
    position = models.CharField(verbose_name='Должность сотрудника',
                                max_length=50)
    category = models.CharField(verbose_name='Категория',
                                choices=CATEGORY_CHOICES,
                                max_length=50,
                                default='employees')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name


class Counter(models.Model):
    contacted = models.PositiveIntegerField(verbose_name='Обратилось')
    discharged = models.PositiveIntegerField(verbose_name='Выписано')
    operated = models.PositiveIntegerField(verbose_name='Прооперировано')
    born = models.PositiveIntegerField(verbose_name='Родилось')

    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчик"

    def save(self, *args, **kwargs):
        if not self.pk and Counter.objects.exists():
            raise ValidationError('Можно создать только одну запись Counter')
        return super(Counter, self).save(*args, **kwargs)

    def __str__(self):
        return 'Счетчик обратившихся, выписанных, оперированных и рожденных'
