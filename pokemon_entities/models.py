from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True),
    title_ru = models.CharField('Название по-русски', max_length=200)
    title_en = models.CharField('Название по-английски', max_length=200, blank=True, null=True)
    title_jp = models.CharField('Название по-японски', max_length=200, blank=True, null=True)
    image = models.ImageField('Картинка', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                           related_name='next_evolution', verbose_name='Предыдущая эволюция')

    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateField('Время появления', blank=True, null=True)
    disappeared_at = models.DateField('Время исчезновения', blank=True, null=True)
    level = models.IntegerField('Уровень')
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)
