# Generated by Django 4.0.2 on 2022-09-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_orderfield_alter_clients_status_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('Ожиданы', 'Ожиданы'), ('Встреча', 'Встреча'), ('Договор', 'Договор'), ('Архив', 'Архив')], default='Ожиданы', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Оплачено', 'Оплачено'), ('Аванс', 'Аванс'), ('Ожидание', 'Ожидание')], default='Ожидание', max_length=120),
        ),
    ]
