# Generated by Django 2.2.5 on 2021-07-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210708_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemsalesrecord',
            name='menuItem',
            field=models.CharField(choices=[('Chocolate Cake', 'Chocolate Cake'), ('Lemon Tart', 'Lemon Tart'), ('Banana Bread', 'Banana Bread'), ('Cinnamon Roll', 'Cinnamon Roll'), ('Croissant', 'Croissant'), ('Apple Pie', 'Apple Pie'), ('Iced Tea', 'Ice Tea'), ('Iced Coffee', 'Iced Coffee'), ('Iced Lemonade', 'Iced Lemonade'), ('Milk Tea', 'Milk Tea')], max_length=100),
        ),
    ]