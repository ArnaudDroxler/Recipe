# Generated by Django 3.0.3 on 2020-03-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0003_auto_20200225_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='note',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
