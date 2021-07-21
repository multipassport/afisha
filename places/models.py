from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0,
        blank=False,
        null=False
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images'
    )

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place.title}'
