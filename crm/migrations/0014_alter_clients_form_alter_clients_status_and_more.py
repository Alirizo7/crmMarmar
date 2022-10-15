# Generated by Django 4.0.2 on 2022-08-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_alter_clients_form_alter_clients_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='form',
            field=models.CharField(choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('Договор', 'Договор'), ('Встреча', 'Встреча'), ('Архив', 'Архив'), ('Ожиданы', 'Ожиданы')], default='Ожиданы', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Ожидание', 'Ожидание'), ('Оплачено', 'Оплачено'), ('Аванс', 'Аванс')], default='Ожидание', max_length=120),
        ),
        migrations.AlterField(
            model_name='projectservice',
            name='parcent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]