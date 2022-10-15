# Generated by Django 4.0.2 on 2022-09-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_projectservice_user_alter_clients_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('field', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('Архив', 'Архив'), ('Встреча', 'Встреча'), ('Договор', 'Договор'), ('Ожиданы', 'Ожиданы')], default='Ожиданы', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Оплачено', 'Оплачено'), ('Ожидание', 'Ожидание'), ('Аванс', 'Аванс')], default='Ожидание', max_length=120),
        ),
    ]
