# Generated by Django 2.2.3 on 2020-04-24 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Название по-русски')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Название по-английски')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Название по-японски')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('previous_evolution', models.ForeignKey(blank=True, default='No evo', on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='Предыдущая эволюция')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateField(blank=True, verbose_name='Время появления')),
                ('disappeared_at', models.DateField(blank=True, verbose_name='Время исчезновения')),
                ('level', models.IntegerField(verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, verbose_name='Сила')),
                ('defence', models.IntegerField(blank=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
