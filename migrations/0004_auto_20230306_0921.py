# Generated by Django 3.1.7 on 2023-03-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_auto_20230303_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_id',
            name='bx_id',
            field=models.CharField(max_length=100),
        ),
    ]