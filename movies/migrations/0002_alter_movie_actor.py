# Generated by Django 5.0.4 on 2024-06-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actor_nationality'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(blank=True, null=True, related_name='movies', to='actors.actor'),
        ),
    ]
