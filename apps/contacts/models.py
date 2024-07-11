from django.db import models

class Contacts(models.Model):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    email = models.EmailField(verbose_name='Электронная почта', max_length=50)
    fax = models.CharField(verbose_name='факс номер', max_length=20)
    instagram = models.CharField(verbose_name='Инстаграм', max_length=255)
    facebook = models.CharField(verbose_name='Фейсбук', max_length=255)
    youtube = models.CharField(verbose_name='Ютуб', max_length=255)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number