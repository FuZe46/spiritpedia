# Generated by Django 5.0.3 on 2024-03-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_game_name_game_game_game_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='game',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/games_logo/'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(related_name='tournaments', to='news.team'),
        ),
    ]
