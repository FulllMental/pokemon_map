# Generated by Django 3.1.14 on 2022-12-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20221203_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='element_image',
            field=models.ImageField(null=True, upload_to='elements', verbose_name='Изображение элемента'),
        ),
    ]
