# Generated by Django 5.0.7 on 2024-11-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event__fkey_teams_event__fkey_away_team_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='_fkey_away_team',
            new_name='fkey_away_team',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='_fkey_home_team',
            new_name='fkey_home_team',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='_fkey_sport',
            new_name='fkey_sport',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='_fkey_venue',
            new_name='fkey_venue',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='_fkey_sport',
            new_name='fkey_sport',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='_fkey_country',
            new_name='fkey_country',
        ),
    ]
