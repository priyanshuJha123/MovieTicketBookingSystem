# Generated by Django 3.0 on 2020-08-28 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_language_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='premier_date',
        ),
    ]