# Generated by Django 2.2.5 on 2021-07-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210708_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrecord',
            name='branchOfOrigin',
            field=models.CharField(choices=[('Selangor', 'Selangor'), ('Johor', 'Johor'), ('Perak', 'Perak')], max_length=100),
        ),
    ]