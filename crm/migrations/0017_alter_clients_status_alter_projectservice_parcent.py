# Generated by Django 4.0.2 on 2022-08-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_alter_clients_status_alter_orders_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('Архив', 'Архив'), ('Встреча', 'Встреча'), ('Договор', 'Договор'), ('Ожиданы', 'Ожиданы')], default='Ожиданы', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='projectservice',
            name='parcent',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
