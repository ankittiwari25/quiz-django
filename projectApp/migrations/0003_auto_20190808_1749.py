# Generated by Django 2.2.1 on 2019-08-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_auto_20190807_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='name',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
