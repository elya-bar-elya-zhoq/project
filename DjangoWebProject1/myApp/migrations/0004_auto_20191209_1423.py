# Generated by Django 3.0 on 2019-12-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20191209_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_author',
            field=models.CharField(max_length=12, verbose_name='Автор предложения'),
        ),
    ]
