# Generated by Django 5.0.4 on 2024-10-01 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_actor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='realese_date',
            new_name='release_date',
        ),
    ]
