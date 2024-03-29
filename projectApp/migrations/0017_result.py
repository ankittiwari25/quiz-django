# Generated by Django 2.0.12 on 2019-09-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0016_auto_20190905_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=250)),
                ('score', models.PositiveIntegerField(max_length=100)),
                ('total', models.PositiveIntegerField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
