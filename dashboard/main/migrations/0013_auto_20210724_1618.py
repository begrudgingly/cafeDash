# Generated by Django 2.2.5 on 2021-07-24 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210710_2126'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]