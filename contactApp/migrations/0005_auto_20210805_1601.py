# Generated by Django 2.2.4 on 2021-08-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0004_auto_20191003_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2021-08-05', max_length=20, verbose_name='出生日期'),
        ),
    ]