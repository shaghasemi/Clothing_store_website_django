# Generated by Django 5.0.1 on 2024-03-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersModule', '0008_alter_usersmodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='نام کاربری'),
        ),
    ]
