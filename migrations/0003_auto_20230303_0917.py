# Generated by Django 3.1.7 on 2023-03-03 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20230303_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_id',
            options={'verbose_name': 'Агенты', 'verbose_name_plural': 'Агенты'},
        ),
    ]
