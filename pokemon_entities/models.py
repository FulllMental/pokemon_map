from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя покемона')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя покемона на японском')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя покемона на английском')
    image = models.ImageField(upload_to='pictures', null=True, verbose_name='Изображение покемона')
    description = models.TextField(max_length=350, blank=True, verbose_name='Описание покемона')
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционировал покемон',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolution',
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    Lat = models.FloatField(verbose_name='Координаты: широта')
    Lon = models.FloatField(verbose_name='Координаты: долгота')
    Appeared_at = models.DateTimeField(verbose_name='Время появления')
    Disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    Level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    Health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    Strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    Defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    Stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')
