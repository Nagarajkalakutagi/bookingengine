# Generated by Django 3.2 on 2021-11-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20211124_0350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlockedDays',
            new_name='Blocked',
        ),
    ]
