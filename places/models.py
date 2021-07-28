from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(
        verbose_name='Короткое описание', blank=True)
    description_long = HTMLField(verbose_name='Описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0,
        blank=True,
        db_index=True,
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
    )

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place.title}'
