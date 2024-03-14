from django.db import models


class Menu(models.Model):
    menu_cell = models.CharField(max_length=100, null=True, verbose_name='Ячейка меню')
    

class GuitaristProgramTepping(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='Заголовок')
    description = models.TextField(null=True, verbose_name='Описание')
    video = models.FileField(upload_to='videos_uploaded', null=True)
    photo = models.ImageField(upload_to='images/photo', null=True, verbose_name='Фотографии')

    class Meta:
        verbose_name = 'Теппинг'
        verbose_name_plural = 'Теппинг'

    def __str__(self):
        return self.title


class GuitaristProgramMediationTechnique(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='Заголовок')
    description = models.TextField(null=True, verbose_name='Описание')
    video = models.FileField(upload_to='videos_uploaded', null=True)
    photo = models.ImageField(upload_to='images/photo', null=True, verbose_name='Фотографии')

    class Meta:
        verbose_name = 'Медиаторная техника'
        verbose_name_plural = 'Медиаторная техника'

    def __str__(self):
        return self.title


class GuitaristProgramAcoustic(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='Заголовок')
    description = models.TextField(null=True, verbose_name='Описание')
    video = models.FileField(upload_to='videos_uploaded', null=True)
    photo = models.ImageField(upload_to='images/photo', null=True, verbose_name='Фотографии')

    class Meta:
        verbose_name = 'Медиаторная техника'
        verbose_name_plural = 'Медиаторная техника'

    def __str__(self):
        return self.title
