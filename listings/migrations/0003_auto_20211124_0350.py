# Generated by Django 3.2 on 2021-11-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_blockeddays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockeddays',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blockeddays',
            name='check_out',
            field=models.DateField(),
        ),
    ]
