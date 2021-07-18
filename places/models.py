from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.CharField(
        max_length=200, verbose_name='Короткое описание'
    )
    description_long = models.TextField(verbose_name='Описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
