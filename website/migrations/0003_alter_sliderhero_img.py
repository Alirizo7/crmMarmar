# Generated by Django 3.2.2 on 2023-03-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_sliderhero_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderhero',
            name='img',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
