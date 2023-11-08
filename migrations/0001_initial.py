# Generated by Django 3.1.7 on 2023-02-21 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Core_Supervizer',
            fields=[
                ('region', models.CharField(choices=[('Чуйская', 'Чуйская'), ('Иссык-Кульская', 'Иссык-Кульская'), ('Нарынская', 'Нарынская'), ('Джалал-Абадская', 'Джалал-Абадская'), ('Баткенская', 'Баткенская'), ('Ошская', 'Ошская'), ('Таласская', 'Таласская')], max_length=50, verbose_name='Область')),
                ('supervizer_id', models.BigIntegerField(verbose_name='Супервайзер_ID')),
                ('supervizer_surname', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ФИО супервайзера')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('tg_id', models.BigIntegerField(blank=True, max_length=200, primary_key=True, serialize=False)),
                ('ticket_title', models.TextField(max_length=200, null=True)),
                ('paystatus', models.TextField(max_length=200, null=True)),
                ('cf_954_tv', models.TextField(max_length=200, null=True)),
                ('cf_968_naim', models.TextField(max_length=200, null=True)),
                ('cf_924_adres', models.TextField(max_length=200, null=True)),
                ('cf_926_router', models.TextField(max_length=200, null=True)),
                ('cf_928_tariff', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('name', models.TextField(max_length=200, null=True)),
                ('surname', models.TextField(max_length=200, null=True)),
                ('number', models.TextField(max_length=200, null=True)),
                ('number2', models.TextField(max_length=200, null=True)),
                ('location', models.TextField(max_length=200, null=True)),
                ('passport', models.TextField(max_length=200, null=True)),
                ('passport2', models.TextField(max_length=200, null=True)),
                ('provider', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_state',
            fields=[
                ('tg_id', models.BigIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='user_id',
            fields=[
                ('bx_id', models.CharField(default=6666, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='Область')),
                ('teleid', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Телеграм_ID')),
                ('supervizer', models.CharField(blank=True, max_length=10)),
                ('surname', models.CharField(max_length=50, verbose_name='ФИО агента')),
                ('hydra_id_sales', models.CharField(blank=True, max_length=50, verbose_name='Гидра_ID')),
                ('supervizer_surname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='super_id', to='agent.core_supervizer', verbose_name='ФИО супервайзера')),
            ],
        ),
    ]