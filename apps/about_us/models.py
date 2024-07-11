from django.db import models
from django.core.exceptions import ValidationError


class Image(models.Model):
    image = models.ImageField(upload_to='about_us/')


class AboutUs(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            raise ValidationError('Можно создать только одну запись AboutUS')
        return super(AboutUs, self).save(*args, **kwargs)

    def __str__(self):
        return self.description[:10]


class History(AboutUs):

    def save(self, *args, **kwargs):
        if not self.pk and History.objects.exists():
            raise ValidationError('Можно создать только одну запись History')
        return super(History, self).save(*args, **kwargs)

    def __str__(self):
        return self.description[:10]


class CenterCharter(AboutUs):

    def save(self, *args, **kwargs):
        if not self.pk and CenterCharter.objects.exists():
            raise ValidationError('Можно создать только одну запись Charter')
        return super(CenterCharter, self).save(*args, **kwargs)

    def __str__(self):
        return self.description[:10]


class Normative(models.Model):
    title = models.CharField(max_length=155)
    pdf = models.FileField()

    def __str__(self):
        return self.title


class PDFFile(models.Model):
    pdf = models.FilePathField()


class Images(models.Model):
    image = models.ImageField(upload_to='science_part/')


class Normative(models.Model):
    title = models.CharField(max_lenght=155),
    pdf = models.FileField()

    def  __str__(self):
        return self.title


class Pdf(models.Model):
    pdf = models.FileField()


class Departments(models.Model):
    title = models.CharField(max_lengh=155)
    description = models.TextField(blank=True, null=True)
    # employe = models.ForeignKey('Employe', blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True)
    pdf = models.ForeignKey(Pdf, blank=True, null=True)

    def __str__(self):
        return self.title